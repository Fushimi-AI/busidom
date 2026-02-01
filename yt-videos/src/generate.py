#!/usr/bin/env python3
"""
YT-Videos Generator

Main CLI tool to generate videos from audio + transcript.

Usage:
    python generate.py --audio recording.mp3 --transcript script.txt --output video.mp4
"""

import click
from pathlib import Path
import tempfile
import shutil

from aligner import AudioAligner, WordTiming
from subtitle import SubtitleGenerator, create_subtitle_config
from renderer import VideoRenderer, create_render_config


@click.command()
@click.option(
    '--audio', '-a',
    required=True,
    type=click.Path(exists=True),
    help='Path to audio file (mp3, wav, etc.)'
)
@click.option(
    '--transcript', '-t',
    type=click.Path(exists=True),
    help='Path to transcript file (optional, improves accuracy)'
)
@click.option(
    '--output', '-o',
    default='output.mp4',
    help='Output video path'
)
@click.option(
    '--format', '-f',
    type=click.Choice(['short', 'long']),
    default='short',
    help='Video format: short (9:16) or long (16:9)'
)
@click.option(
    '--quality', '-q',
    type=click.Choice(['fast', 'medium', 'high']),
    default='medium',
    help='Render quality (affects speed)'
)
@click.option(
    '--font-size',
    type=int,
    default=None,
    help='Font size override'
)
@click.option(
    '--highlight-color',
    default='yellow',
    help='Highlight color (yellow, cyan, green, red, white)'
)
@click.option(
    '--model',
    type=click.Choice(['tiny', 'base', 'small', 'medium', 'large-v3']),
    default='base',
    help='Whisper model size (larger = more accurate, slower)'
)
@click.option(
    '--keep-temp',
    is_flag=True,
    help='Keep temporary files (for debugging)'
)
def generate(
    audio: str,
    transcript: str,
    output: str,
    format: str,
    quality: str,
    font_size: int,
    highlight_color: str,
    model: str,
    keep_temp: bool
):
    """
    Generate a video with word-by-word highlighting from audio.
    
    Takes an audio file and optional transcript, then creates a video
    with white text on black background where each word highlights
    as it's spoken.
    """
    
    click.echo("=" * 50)
    click.echo("YT-Videos Generator")
    click.echo("=" * 50)
    
    # Create temp directory
    temp_dir = Path(tempfile.mkdtemp(prefix="ytvideo_"))
    subtitle_path = temp_dir / "subtitles.ass"
    
    try:
        # Step 1: Align audio to get word timestamps
        click.echo(f"\n📝 Step 1/3: Extracting word timestamps...")
        click.echo(f"   Loading Whisper model '{model}'...")
        
        aligner = AudioAligner(model_size=model)
        
        # Load transcript if provided
        transcript_text = None
        if transcript:
            transcript_text = Path(transcript).read_text().strip()
            click.echo(f"   Using provided transcript ({len(transcript_text)} chars)")
        
        # Align
        click.echo(f"   Processing audio: {audio}")
        if transcript_text:
            result = aligner.align_with_transcript(audio, transcript_text)
        else:
            result = aligner.align(audio)
        
        click.echo(f"   ✓ Found {len(result.words)} words")
        click.echo(f"   ✓ Duration: {result.duration:.1f} seconds")
        
        # Preview first few words
        if result.words:
            preview = result.words[:5]
            preview_text = " ".join(w.word for w in preview)
            click.echo(f"   Preview: \"{preview_text}...\"")
        
        # Step 2: Generate subtitles
        click.echo(f"\n📄 Step 2/3: Generating subtitles...")
        
        sub_config = create_subtitle_config(
            format=format,
            font_size=font_size,
            highlight_color=highlight_color
        )
        
        generator = SubtitleGenerator(sub_config)
        generator.generate(result.words, str(subtitle_path))
        
        click.echo(f"   ✓ Subtitle file created")
        
        # Step 3: Render video
        click.echo(f"\n🎬 Step 3/3: Rendering video...")
        click.echo(f"   Format: {format} ({'1080x1920' if format == 'short' else '1920x1080'})")
        click.echo(f"   Quality: {quality}")
        
        render_config = create_render_config(format=format, quality=quality)
        renderer = VideoRenderer(render_config)
        
        renderer.render(
            audio_path=audio,
            subtitle_path=str(subtitle_path),
            output_path=output,
            duration=result.duration
        )
        
        click.echo(f"   ✓ Video rendered")
        
        # Done
        click.echo("\n" + "=" * 50)
        click.echo(f"✅ Done! Video saved to: {output}")
        click.echo("=" * 50)
        
        # Show file info
        output_size = Path(output).stat().st_size / (1024 * 1024)
        click.echo(f"\n📊 Output: {output_size:.1f} MB")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        raise click.Abort()
    
    finally:
        # Cleanup temp files
        if not keep_temp:
            shutil.rmtree(temp_dir, ignore_errors=True)
        else:
            click.echo(f"\n🗂️  Temp files kept at: {temp_dir}")


@click.command()
@click.argument('audio', type=click.Path(exists=True))
def preview(audio: str):
    """
    Preview word timestamps without generating video.
    
    Useful for checking alignment before full render.
    """
    click.echo(f"Loading Whisper model...")
    aligner = AudioAligner(model_size="base")
    
    click.echo(f"Processing: {audio}")
    result = aligner.align(audio)
    
    click.echo(f"\nDuration: {result.duration:.2f}s")
    click.echo(f"Words: {len(result.words)}")
    click.echo(f"\nTimestamps:")
    click.echo("-" * 40)
    
    for word in result.words:
        click.echo(f"{word.start:6.2f}s - {word.end:6.2f}s : {word.word}")


# CLI group
@click.group()
def cli():
    """YT-Videos: Generate text videos from audio."""
    pass


cli.add_command(generate, name='generate')
cli.add_command(preview, name='preview')


# Allow running generate directly
if __name__ == '__main__':
    # If called directly, run generate command
    generate()
