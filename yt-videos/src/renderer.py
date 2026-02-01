"""
Video Renderer using FFmpeg

Renders final video from audio + subtitles.
"""

import subprocess
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
from enum import Enum


class VideoFormat(Enum):
    """Video format/aspect ratio."""
    SHORT = "short"  # 9:16 (1080x1920) - YouTube Shorts, TikTok
    LONG = "long"    # 16:9 (1920x1080) - Standard YouTube


@dataclass
class RenderConfig:
    """Video rendering configuration."""
    format: VideoFormat = VideoFormat.SHORT
    fps: int = 30
    background_color: str = "black"
    video_codec: str = "libx264"
    audio_codec: str = "aac"
    audio_bitrate: str = "192k"
    crf: int = 23  # Quality (lower = better, 18-28 range)
    preset: str = "medium"  # Encoding speed (ultrafast to veryslow)
    
    @property
    def width(self) -> int:
        return 1080 if self.format == VideoFormat.SHORT else 1920
    
    @property
    def height(self) -> int:
        return 1920 if self.format == VideoFormat.SHORT else 1080


class VideoRenderer:
    """
    Renders video using FFmpeg.
    
    Combines:
    - Black background
    - Audio file
    - ASS subtitles (burned in)
    """
    
    def __init__(self, config: Optional[RenderConfig] = None):
        self.config = config or RenderConfig()
        self._check_ffmpeg()
    
    def _check_ffmpeg(self):
        """Verify FFmpeg is installed."""
        if not shutil.which("ffmpeg"):
            raise RuntimeError(
                "FFmpeg not found. Please install it:\n"
                "  macOS: brew install ffmpeg\n"
                "  Ubuntu: sudo apt-get install ffmpeg\n"
                "  Windows: https://ffmpeg.org/download.html"
            )
    
    def render(
        self,
        audio_path: str,
        subtitle_path: str,
        output_path: str,
        duration: Optional[float] = None
    ) -> str:
        """
        Render video with audio and subtitles.
        
        Args:
            audio_path: Path to audio file
            subtitle_path: Path to .ass subtitle file
            output_path: Where to save the video
            duration: Optional duration override (seconds)
        
        Returns:
            Path to rendered video
        """
        c = self.config
        
        # Escape subtitle path for FFmpeg filter
        # On Windows, need to escape colons and backslashes
        sub_path_escaped = subtitle_path.replace("\\", "/").replace(":", "\\:")
        
        # Build FFmpeg command
        cmd = [
            "ffmpeg",
            "-y",  # Overwrite output
            
            # Input 1: Generate black background
            "-f", "lavfi",
            "-i", f"color=c={c.background_color}:s={c.width}x{c.height}:r={c.fps}",
            
            # Input 2: Audio file
            "-i", audio_path,
            
            # Video filter: burn in subtitles
            "-vf", f"subtitles='{sub_path_escaped}'",
            
            # Match duration to audio
            "-shortest",
            
            # Video encoding
            "-c:v", c.video_codec,
            "-preset", c.preset,
            "-crf", str(c.crf),
            "-pix_fmt", "yuv420p",  # Compatibility
            
            # Audio encoding
            "-c:a", c.audio_codec,
            "-b:a", c.audio_bitrate,
            
            # Output
            output_path
        ]
        
        # Add duration limit if specified
        if duration:
            cmd.insert(1, "-t")
            cmd.insert(2, str(duration + 1))  # Small buffer
        
        # Run FFmpeg
        print(f"  Running FFmpeg...")
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True
        )
        
        if result.returncode != 0:
            error_msg = result.stderr[-2000:] if len(result.stderr) > 2000 else result.stderr
            raise RuntimeError(f"FFmpeg failed:\n{error_msg}")
        
        return output_path
    
    def render_simple(
        self,
        audio_path: str,
        text: str,
        output_path: str
    ) -> str:
        """
        Simple render with static centered text (no animation).
        
        Useful for testing or when subtitles fail.
        """
        c = self.config
        
        # Escape text for FFmpeg
        escaped_text = (
            text
            .replace("\\", "\\\\")
            .replace("'", "'\\''")
            .replace(":", "\\:")
        )
        
        cmd = [
            "ffmpeg",
            "-y",
            "-f", "lavfi",
            "-i", f"color=c={c.background_color}:s={c.width}x{c.height}:r={c.fps}",
            "-i", audio_path,
            "-vf", f"drawtext=fontsize=60:fontcolor=white:x=(w-text_w)/2:y=(h-text_h)/2:text='{escaped_text}'",
            "-shortest",
            "-c:v", c.video_codec,
            "-c:a", c.audio_codec,
            output_path
        ]
        
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode != 0:
            raise RuntimeError(f"FFmpeg failed: {result.stderr}")
        
        return output_path


def create_render_config(
    format: str = "short",
    quality: str = "medium"
) -> RenderConfig:
    """
    Create render config.
    
    Args:
        format: "short" or "long"
        quality: "fast", "medium", or "high"
    
    Returns:
        RenderConfig
    """
    video_format = VideoFormat.SHORT if format == "short" else VideoFormat.LONG
    
    preset_map = {
        "fast": ("ultrafast", 28),
        "medium": ("medium", 23),
        "high": ("slow", 18)
    }
    
    preset, crf = preset_map.get(quality, ("medium", 23))
    
    return RenderConfig(
        format=video_format,
        preset=preset,
        crf=crf
    )


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 4:
        print("Usage: python renderer.py <audio.mp3> <subtitles.ass> <output.mp4>")
        sys.exit(1)
    
    audio = sys.argv[1]
    subs = sys.argv[2]
    output = sys.argv[3]
    
    config = create_render_config("short", "medium")
    renderer = VideoRenderer(config)
    
    print(f"Rendering video...")
    renderer.render(audio, subs, output)
    print(f"Done: {output}")
