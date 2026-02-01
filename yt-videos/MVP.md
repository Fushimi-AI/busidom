# YT-Videos MVP

## Summary

**Input:** Audio file + Transcript text  
**Output:** MP4 video with word-by-word highlighting  
**Stack:** Python + Whisper + FFmpeg  
**Time to build:** ~2-3 hours

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        PIPELINE                              │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐             │
│   │  AUDIO   │    │ WHISPER  │    │   ASS    │             │
│   │  .mp3    │───►│ ALIGNER  │───►│ SUBTITLE │             │
│   │          │    │          │    │          │             │
│   └──────────┘    └──────────┘    └──────────┘             │
│        +                │               │                   │
│   ┌──────────┐          │               │                   │
│   │TRANSCRIPT│          │               │                   │
│   │  .txt    │──────────┘               │                   │
│   └──────────┘                          ▼                   │
│                              ┌──────────────────┐           │
│                              │     FFMPEG       │           │
│                              │   RENDERER       │           │
│                              │                  │           │
│                              │ Black BG + Audio │           │
│                              │ + Karaoke Subs   │           │
│                              └────────┬─────────┘           │
│                                       │                     │
│                                       ▼                     │
│                              ┌──────────────────┐           │
│                              │    OUTPUT.MP4    │           │
│                              │                  │           │
│                              │ Word highlighting│           │
│                              │ synced to audio  │           │
│                              └──────────────────┘           │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Components

### 1. AudioAligner (`aligner.py`)

Uses `faster-whisper` to extract word-level timestamps from audio.

**Input:** Audio file (mp3/wav) + optional transcript  
**Output:** List of `WordTiming(word, start, end)`

Key features:
- Uses Whisper's built-in word timestamps
- Optional transcript alignment for better accuracy
- VAD filter to handle silence

### 2. SubtitleGenerator (`subtitle.py`)

Generates ASS subtitle files with karaoke effects.

**Input:** List of word timings  
**Output:** `.ass` file with `\kf` tags

Key features:
- Karaoke-style smooth fill highlighting
- Auto-groups words into readable lines
- Configurable colors, fonts, sizes

### 3. VideoRenderer (`renderer.py`)

Uses FFmpeg to combine everything into final video.

**Input:** Audio file + ASS subtitle file  
**Output:** MP4 video

Key features:
- Black background generation
- Subtitle burning with ASS
- Support for 9:16 (shorts) and 16:9 (long)

### 4. CLI (`generate.py`)

Main entry point with Click CLI.

```bash
python generate.py \
    --audio recording.mp3 \
    --transcript script.txt \
    --output video.mp4 \
    --format short
```

---

## Usage

### Basic
```bash
python src/generate.py -a audio.mp3 -o video.mp4
```

### With Transcript (more accurate)
```bash
python src/generate.py -a audio.mp3 -t transcript.txt -o video.mp4
```

### YouTube Short (9:16)
```bash
python src/generate.py -a audio.mp3 -f short -o short.mp4
```

### YouTube Long (16:9)
```bash
python src/generate.py -a audio.mp3 -f long -o video.mp4
```

### High Quality
```bash
python src/generate.py -a audio.mp3 -q high -o hq_video.mp4
```

### Custom Styling
```bash
python src/generate.py -a audio.mp3 \
    --font-size 100 \
    --highlight-color cyan \
    -o styled.mp4
```

---

## File Structure

```
yt-videos/
├── README.md           # Quick start guide
├── MVP.md              # This file
├── requirements.txt    # Python dependencies
├── test.sh            # Test script
└── src/
    ├── __init__.py
    ├── generate.py     # Main CLI
    ├── aligner.py      # Whisper word alignment
    ├── subtitle.py     # ASS subtitle generation
    └── renderer.py     # FFmpeg video rendering
```

---

## Dependencies

### Python
```
faster-whisper>=1.0.0   # Word-level speech recognition
pydub>=0.25.1          # Audio processing
click>=8.1.0           # CLI framework
```

### System
```
ffmpeg                  # Video/audio processing
```

---

## Visual Output

```
┌────────────────────────────────────┐
│                                    │
│                                    │
│                                    │
│                                    │
│          The best part             │
│            is no [PART].           │  ← "PART" highlighted yellow
│                                    │
│                                    │
│                                    │
│                                    │
└────────────────────────────────────┘
        Black (#000000) background
        White (#FFFFFF) text
        Yellow (#FFD700) highlight
```

---

## Performance

| Audio Length | Whisper (base) | Render | Total |
|--------------|----------------|--------|-------|
| 30 sec | ~10s | ~15s | ~25s |
| 1 min | ~15s | ~30s | ~45s |
| 5 min | ~45s | ~2min | ~3min |

*On M1 MacBook Pro*

---

## Limitations (MVP)

1. **Single language** - English works best with Whisper
2. **No background music** - Voice only
3. **Fixed styling** - White text on black
4. **Local only** - No cloud processing

---

## Future Enhancements

### P1 (Next)
- [ ] Background music with ducking
- [ ] Custom fonts (TTF upload)
- [ ] Batch processing

### P2 (Later)
- [ ] LLM script generation
- [ ] Multiple highlight styles
- [ ] Animated transitions
- [ ] Web UI
