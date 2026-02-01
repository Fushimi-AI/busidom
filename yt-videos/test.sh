#!/bin/bash
# Quick test script for YT-Videos

set -e

echo "=== YT-Videos Test ==="
echo ""

# Check dependencies
echo "Checking dependencies..."

if ! command -v ffmpeg &> /dev/null; then
    echo "❌ FFmpeg not found. Install with: brew install ffmpeg"
    exit 1
fi
echo "✓ FFmpeg found"

if ! python3 -c "import faster_whisper" &> /dev/null; then
    echo "⚠️  faster-whisper not installed. Run: pip install -r requirements.txt"
fi

# Create test audio (requires say command on macOS)
TEST_DIR="test_output"
mkdir -p "$TEST_DIR"

echo ""
echo "Creating test audio..."
if command -v say &> /dev/null; then
    # macOS
    say -o "$TEST_DIR/test_audio.aiff" "The best part is no part. The best process is no process."
    ffmpeg -y -i "$TEST_DIR/test_audio.aiff" "$TEST_DIR/test_audio.mp3" 2>/dev/null
    rm "$TEST_DIR/test_audio.aiff"
    echo "✓ Test audio created: $TEST_DIR/test_audio.mp3"
else
    echo "⚠️  'say' command not available (macOS only)"
    echo "   Please provide your own test audio file"
    echo ""
    echo "Usage:"
    echo "  python src/generate.py -a your_audio.mp3 -o output.mp4"
    exit 0
fi

# Create test transcript
echo "The best part is no part. The best process is no process." > "$TEST_DIR/test_transcript.txt"
echo "✓ Test transcript created"

echo ""
echo "Running generator..."
cd "$(dirname "$0")"
python src/generate.py \
    --audio "$TEST_DIR/test_audio.mp3" \
    --transcript "$TEST_DIR/test_transcript.txt" \
    --output "$TEST_DIR/test_video.mp4" \
    --format short \
    --model tiny

echo ""
echo "=== Test Complete ==="
echo "Output: $TEST_DIR/test_video.mp4"
