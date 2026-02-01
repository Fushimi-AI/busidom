# YT-Videos: Audio to Video Generator

Local tool to create text-based videos from audio + transcript.

## What It Does

```
Audio (.mp3/.wav) + Transcript (.txt)
              ↓
    Whisper (word alignment)
              ↓
    ASS Subtitles (karaoke style)
              ↓
    FFmpeg (video render)
              ↓
    Video (.mp4) with word highlighting
```

## Quick Start

```bash
# Install
pip install -r requirements.txt

# Generate video
python src/generate.py \
    --audio my_audio.mp3 \
    --transcript my_script.txt \
    --output output.mp4 \
    --format short
```

## Features

- **Word-by-word highlighting** - Words light up as spoken
- **Two formats** - Shorts (9:16) or Long (16:9)
- **Fully local** - No API keys needed
- **Fast** - Uses faster-whisper for speed

## Requirements

- Python 3.10+
- FFmpeg installed
- ~2GB disk for Whisper model (first run)

## Installation

```bash
cd yt-videos
pip install -r requirements.txt

# macOS: Install FFmpeg
brew install ffmpeg

# Ubuntu: Install FFmpeg
sudo apt-get install ffmpeg
```

## Usage Examples

### Short Video (9:16 for YouTube Shorts/TikTok)
```bash
python src/generate.py -a audio.mp3 -t script.txt -f short -o short.mp4
```

### Long Video (16:9 for YouTube)
```bash
python src/generate.py -a audio.mp3 -t script.txt -f long -o video.mp4
```

### Custom Styling
```bash
python src/generate.py -a audio.mp3 -t script.txt \
    --font-size 80 \
    --highlight-color yellow \
    -o styled.mp4
```

## Project Structure

```
yt-videos/
├── README.md
├── requirements.txt
└── src/
    ├── generate.py          # Main CLI
    ├── aligner.py           # Whisper word alignment
    ├── subtitle.py          # ASS subtitle generation
    └── renderer.py          # FFmpeg video rendering
```
