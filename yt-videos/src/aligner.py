"""
Audio-Text Aligner using Whisper

Extracts word-level timestamps from audio file.
"""

from dataclasses import dataclass
from typing import List, Optional
from faster_whisper import WhisperModel


@dataclass
class WordTiming:
    """Single word with timing information."""
    word: str
    start: float  # seconds
    end: float    # seconds


@dataclass 
class AlignmentResult:
    """Result of audio-text alignment."""
    words: List[WordTiming]
    duration: float
    transcript: str


class AudioAligner:
    """
    Aligns audio with transcript to get word-level timestamps.
    Uses Whisper for speech recognition with word timestamps.
    """
    
    def __init__(
        self, 
        model_size: str = "base",
        device: str = "auto",
        compute_type: str = "auto"
    ):
        """
        Initialize the aligner.
        
        Args:
            model_size: Whisper model size (tiny, base, small, medium, large-v3)
            device: Device to use (auto, cpu, cuda)
            compute_type: Compute type (auto, int8, float16, float32)
        """
        self.model = WhisperModel(
            model_size, 
            device=device,
            compute_type=compute_type
        )
    
    def align(
        self, 
        audio_path: str,
        transcript: Optional[str] = None
    ) -> AlignmentResult:
        """
        Get word-level timestamps from audio.
        
        Args:
            audio_path: Path to audio file (mp3, wav, etc.)
            transcript: Optional transcript (for reference, not used in alignment yet)
        
        Returns:
            AlignmentResult with word timings
        """
        # Transcribe with word timestamps
        segments, info = self.model.transcribe(
            audio_path,
            word_timestamps=True,
            vad_filter=True  # Filter out silence
        )
        
        words = []
        full_transcript = []
        
        for segment in segments:
            full_transcript.append(segment.text)
            
            if segment.words:
                for word_info in segment.words:
                    words.append(WordTiming(
                        word=word_info.word.strip(),
                        start=word_info.start,
                        end=word_info.end
                    ))
        
        return AlignmentResult(
            words=words,
            duration=info.duration,
            transcript=" ".join(full_transcript)
        )
    
    def align_with_transcript(
        self,
        audio_path: str,
        transcript: str
    ) -> AlignmentResult:
        """
        Align audio with provided transcript.
        
        Uses Whisper to get timestamps, then maps to provided transcript.
        This helps when transcript differs from Whisper output.
        
        Args:
            audio_path: Path to audio file
            transcript: The known correct transcript
        
        Returns:
            AlignmentResult with word timings matched to transcript
        """
        # Get Whisper's word timings
        result = self.align(audio_path)
        
        # If transcript provided, try to align words
        if transcript:
            transcript_words = transcript.split()
            whisper_words = [w.word for w in result.words]
            
            # Simple alignment: use Whisper timings if word counts match roughly
            # TODO: Implement fuzzy matching for better alignment
            if abs(len(transcript_words) - len(whisper_words)) <= len(transcript_words) * 0.1:
                # Close enough, use transcript words with Whisper timings
                aligned_words = []
                for i, timing in enumerate(result.words):
                    if i < len(transcript_words):
                        aligned_words.append(WordTiming(
                            word=transcript_words[i],
                            start=timing.start,
                            end=timing.end
                        ))
                
                return AlignmentResult(
                    words=aligned_words,
                    duration=result.duration,
                    transcript=transcript
                )
        
        # Fall back to Whisper's transcription
        return result


def get_aligner(model_size: str = "base") -> AudioAligner:
    """Factory function to create an AudioAligner."""
    return AudioAligner(model_size=model_size)


# Example usage
if __name__ == "__main__":
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python aligner.py <audio_file>")
        sys.exit(1)
    
    audio_path = sys.argv[1]
    
    print(f"Loading Whisper model...")
    aligner = AudioAligner(model_size="base")
    
    print(f"Aligning audio: {audio_path}")
    result = aligner.align(audio_path)
    
    print(f"\nDuration: {result.duration:.2f}s")
    print(f"Words found: {len(result.words)}")
    print(f"\nWord timings:")
    for word in result.words[:20]:  # First 20 words
        print(f"  {word.start:.2f}s - {word.end:.2f}s: '{word.word}'")
    
    if len(result.words) > 20:
        print(f"  ... and {len(result.words) - 20} more words")
