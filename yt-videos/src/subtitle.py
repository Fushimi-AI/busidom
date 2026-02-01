"""
ASS Subtitle Generator with Karaoke-Style Word Highlighting

Generates .ass subtitle files with word-by-word highlighting effects.
"""

from dataclasses import dataclass
from typing import List, Optional
from pathlib import Path


@dataclass
class WordTiming:
    """Single word with timing."""
    word: str
    start: float
    end: float


@dataclass
class SubtitleConfig:
    """Configuration for subtitle generation."""
    # Video dimensions
    width: int = 1080
    height: int = 1920
    
    # Typography
    font_name: str = "Arial"
    font_size: int = 80
    bold: bool = True
    
    # Colors (ASS format: &HBBGGRR - BGR not RGB!)
    normal_color: str = "&HFFFFFF"      # White
    highlight_color: str = "&H00D7FF"   # Yellow/Gold (BGR)
    outline_color: str = "&H000000"     # Black outline
    
    # Layout
    margin_v: int = 50       # Vertical margin
    max_words_per_line: int = 4
    alignment: int = 5       # Center (ASS alignment: 5 = center)
    
    # Effects
    outline_width: int = 3
    shadow: int = 0


class SubtitleGenerator:
    """
    Generates ASS subtitles with karaoke-style word highlighting.
    """
    
    def __init__(self, config: Optional[SubtitleConfig] = None):
        self.config = config or SubtitleConfig()
    
    def generate(
        self, 
        words: List[WordTiming], 
        output_path: str
    ) -> str:
        """
        Generate ASS subtitle file.
        
        Args:
            words: List of words with timing
            output_path: Where to save the .ass file
        
        Returns:
            Path to generated file
        """
        content = self._build_header()
        content += self._build_styles()
        content += self._build_events(words)
        
        Path(output_path).write_text(content, encoding='utf-8')
        return output_path
    
    def _build_header(self) -> str:
        """Build ASS header section."""
        return f"""[Script Info]
Title: YT-Videos Generated Subtitles
ScriptType: v4.00+
PlayResX: {self.config.width}
PlayResY: {self.config.height}
WrapStyle: 0
ScaledBorderAndShadow: yes

"""
    
    def _build_styles(self) -> str:
        """Build ASS styles section."""
        c = self.config
        return f"""[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Default,{c.font_name},{c.font_size},{c.normal_color},{c.highlight_color},{c.outline_color},&H00000000,{1 if c.bold else 0},0,0,0,100,100,0,0,1,{c.outline_width},{c.shadow},{c.alignment},10,10,{c.margin_v},1

"""
    
    def _build_events(self, words: List[WordTiming]) -> str:
        """Build ASS events (dialogue lines) with karaoke effects."""
        events = "[Events]\n"
        events += "Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text\n"
        
        # Group words into lines
        lines = self._group_words(words)
        
        for line_words in lines:
            if not line_words:
                continue
            
            # Line timing
            line_start = line_words[0].start
            line_end = line_words[-1].end + 0.3  # Small buffer
            
            # Build karaoke text
            karaoke_text = self._build_karaoke_line(line_words, line_start)
            
            # Format times
            start_str = self._format_time(line_start)
            end_str = self._format_time(line_end)
            
            events += f"Dialogue: 0,{start_str},{end_str},Default,,0,0,0,,{karaoke_text}\n"
        
        return events
    
    def _group_words(self, words: List[WordTiming]) -> List[List[WordTiming]]:
        """
        Group words into display lines.
        
        Groups by:
        1. Max words per line
        2. Natural pauses (gaps > 0.5s)
        """
        lines = []
        current_line = []
        
        for i, word in enumerate(words):
            current_line.append(word)
            
            # Check if we should break
            should_break = False
            
            # Max words reached
            if len(current_line) >= self.config.max_words_per_line:
                should_break = True
            
            # Natural pause (gap before next word)
            if i < len(words) - 1:
                gap = words[i + 1].start - word.end
                if gap > 0.5:
                    should_break = True
            
            if should_break:
                lines.append(current_line)
                current_line = []
        
        # Don't forget last line
        if current_line:
            lines.append(current_line)
        
        return lines
    
    def _build_karaoke_line(
        self, 
        words: List[WordTiming], 
        line_start: float
    ) -> str:
        """
        Build karaoke text with \\kf tags.
        
        \\kf = smooth fill karaoke effect
        Number after \\kf = duration in centiseconds
        """
        parts = []
        current_time = line_start
        
        for i, word in enumerate(words):
            # Gap before word (silence)
            gap = word.start - current_time
            if gap > 0.01:  # Only if significant gap
                gap_cs = max(1, int(gap * 100))
                parts.append(f"{{\\kf{gap_cs}}}")
            
            # Word duration
            duration = word.end - word.start
            duration_cs = max(1, int(duration * 100))
            
            # Add word with karaoke tag
            parts.append(f"{{\\kf{duration_cs}}}{word.word}")
            
            # Add space (except last word)
            if i < len(words) - 1:
                parts.append(" ")
            
            current_time = word.end
        
        return "".join(parts)
    
    def _format_time(self, seconds: float) -> str:
        """
        Format time for ASS: H:MM:SS.cc (centiseconds)
        """
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        centisecs = int((seconds % 1) * 100)
        
        return f"{hours}:{minutes:02d}:{secs:02d}.{centisecs:02d}"


def create_subtitle_config(
    format: str = "short",
    font_size: Optional[int] = None,
    highlight_color: Optional[str] = None
) -> SubtitleConfig:
    """
    Create subtitle config for video format.
    
    Args:
        format: "short" (9:16) or "long" (16:9)
        font_size: Override font size
        highlight_color: Override highlight color (name or hex)
    
    Returns:
        SubtitleConfig
    """
    if format == "short":
        config = SubtitleConfig(
            width=1080,
            height=1920,
            font_size=font_size or 80,
            max_words_per_line=3
        )
    else:  # long
        config = SubtitleConfig(
            width=1920,
            height=1080,
            font_size=font_size or 64,
            max_words_per_line=5
        )
    
    # Handle color overrides
    if highlight_color:
        color_map = {
            "yellow": "&H00D7FF",
            "gold": "&H00D7FF", 
            "cyan": "&HFFFF00",
            "green": "&H00FF00",
            "red": "&H0000FF",
            "white": "&HFFFFFF",
        }
        config.highlight_color = color_map.get(
            highlight_color.lower(), 
            highlight_color
        )
    
    return config


# Example usage
if __name__ == "__main__":
    # Test data
    test_words = [
        WordTiming("The", 0.0, 0.2),
        WordTiming("best", 0.25, 0.5),
        WordTiming("part", 0.55, 0.8),
        WordTiming("is", 0.85, 1.0),
        WordTiming("no", 1.1, 1.3),
        WordTiming("part.", 1.35, 1.7),
    ]
    
    # Generate
    config = create_subtitle_config("short")
    generator = SubtitleGenerator(config)
    generator.generate(test_words, "test.ass")
    
    print("Generated test.ass")
    print(Path("test.ass").read_text())
