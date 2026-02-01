# YouTube Automation: Technical Implementation

**Goal:** Automate Founders Podcast-style content creation from book → video

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                         AUTOMATION PIPELINE                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐     │
│  │  BOOK    │    │ ANALYSIS │    │  SCRIPT  │    │  AUDIO   │     │
│  │  INPUT   │───►│  ENGINE  │───►│  WRITER  │───►│ GENERATOR│     │
│  │          │    │          │    │          │    │          │     │
│  │ PDF/EPUB │    │ Claude   │    │ GPT-4/   │    │ Eleven   │     │
│  │ Transcript│    │ 200K ctx │    │ Claude   │    │ Labs     │     │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘     │
│                                                       │             │
│                                                       ▼             │
│  ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐     │
│  │ PUBLISH  │◄───│  VIDEO   │◄───│ THUMBNAIL│◄───│  AUDIO   │     │
│  │          │    │ CREATOR  │    │ GENERATOR│    │  FILE    │     │
│  │ YouTube  │    │ CapCut/  │    │ Canva/   │    │  .mp3    │     │
│  │ API      │    │ InVideo  │    │ Midjourney│    │          │     │
│  └──────────┘    └──────────┘    └──────────┘    └──────────┘     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Module 1: Book Analysis Engine

### Purpose
Extract insights, principles, and quotes from books using Claude's 200K context.

### book_analyzer.py

```python
"""
Book Analysis Engine
Extracts entrepreneur principles from biographies using Claude.
"""

import anthropic
import json
from pathlib import Path
import PyPDF2
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Principle:
    name: str
    insight: str
    quote: str
    story: str
    application: str
    
@dataclass
class BookAnalysis:
    entrepreneur: str
    book_title: str
    author: str
    principles: List[Principle]
    key_themes: List[str]
    memorable_quotes: List[str]

class BookAnalyzer:
    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"
    
    def extract_text_from_pdf(self, pdf_path: str) -> str:
        """Extract text content from PDF file."""
        text = ""
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        return text
    
    def analyze_book(
        self, 
        content: str, 
        entrepreneur: str,
        book_title: str,
        author: str
    ) -> BookAnalysis:
        """Analyze book content and extract principles."""
        
        prompt = f"""You are analyzing "{book_title}" by {author} about {entrepreneur}.

Your task: Extract the most valuable COMPANY-BUILDING principles that entrepreneurs can apply today.

## EXTRACTION GUIDELINES

Focus ONLY on:
- How {entrepreneur} built companies
- Decision-making frameworks and mental models
- Leadership and management principles
- Execution strategies and tactics
- What made them different from others

Ignore:
- Personal life details (unless directly relevant to business success)
- Historical context that isn't actionable
- Surface-level biographical facts

## OUTPUT FORMAT

For each principle (extract 8-12 of the BEST):

### Principle: [NAME] (3-5 words)

**Core Insight:** [One sentence that captures the essence]

**The Story:** [2-3 paragraphs telling the specific story/example from the book that illustrates this]

**Key Quote:** "[Direct quote from the book that captures this principle]"

**Why This Matters Today:** [1 paragraph on how entrepreneurs can apply this NOW]

**Actionable Takeaway:** [Specific action someone can take]

---

Also provide:
1. 5 KEY THEMES that run through {entrepreneur}'s approach
2. 10 MEMORABLE QUOTES (with context)

## BOOK CONTENT

{content[:180000]}
"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=8000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Parse response into structured data
        return self._parse_response(
            response.content[0].text,
            entrepreneur,
            book_title,
            author
        )
    
    def _parse_response(
        self, 
        response: str, 
        entrepreneur: str,
        book_title: str,
        author: str
    ) -> BookAnalysis:
        """Parse Claude's response into structured BookAnalysis."""
        # For MVP, return raw response
        # TODO: Implement proper parsing
        return BookAnalysis(
            entrepreneur=entrepreneur,
            book_title=book_title,
            author=author,
            principles=[],  # Parse from response
            key_themes=[],  # Parse from response
            memorable_quotes=[]  # Parse from response
        )
    
    def save_analysis(self, analysis: BookAnalysis, output_path: str):
        """Save analysis to JSON file."""
        with open(output_path, 'w') as f:
            json.dump(analysis.__dict__, f, indent=2)


# Usage example
if __name__ == "__main__":
    analyzer = BookAnalyzer()
    
    # Load book
    book_text = analyzer.extract_text_from_pdf("elon_musk_biography.pdf")
    
    # Analyze
    analysis = analyzer.analyze_book(
        content=book_text,
        entrepreneur="Elon Musk",
        book_title="Elon Musk",
        author="Walter Isaacson"
    )
    
    # Save
    analyzer.save_analysis(analysis, "elon_analysis.json")
```

---

## Module 2: Script Generator

### Purpose
Transform book analysis into podcast-style script.

### script_generator.py

```python
"""
Script Generator
Creates Founders Podcast-style scripts from book analysis.
"""

import anthropic
from dataclasses import dataclass
from typing import List, Optional
import json

@dataclass
class ScriptSection:
    section_type: str  # hook, context, principle, synthesis
    content: str
    duration_estimate: int  # seconds

@dataclass
class PodcastScript:
    title: str
    entrepreneur: str
    total_duration: int  # seconds
    sections: List[ScriptSection]
    full_script: str

class ScriptGenerator:
    def __init__(self, api_key: Optional[str] = None):
        self.client = anthropic.Anthropic(api_key=api_key)
        self.model = "claude-sonnet-4-20250514"
    
    def generate_script(
        self,
        analysis_path: str,
        target_duration: int = 45,  # minutes
        style: str = "founders_podcast"
    ) -> PodcastScript:
        """Generate podcast script from book analysis."""
        
        # Load analysis
        with open(analysis_path, 'r') as f:
            analysis = json.load(f)
        
        # Style templates
        styles = {
            "founders_podcast": self._founders_style_prompt(),
            "educational": self._educational_style_prompt(),
            "storytelling": self._storytelling_style_prompt()
        }
        
        prompt = f"""{styles[style]}

## BOOK ANALYSIS
Entrepreneur: {analysis['entrepreneur']}
Book: {analysis['book_title']} by {analysis['author']}

{json.dumps(analysis, indent=2)}

## REQUIREMENTS
- Target duration: {target_duration} minutes (~{target_duration * 150} words)
- Must be spoken content (not written article)
- Include natural pauses, emphasis markers
- Read quotes dramatically

## OUTPUT
Write the complete podcast script, ready for voice generation.
"""

        response = self.client.messages.create(
            model=self.model,
            max_tokens=12000,
            messages=[{"role": "user", "content": prompt}]
        )
        
        script_text = response.content[0].text
        
        return PodcastScript(
            title=f"How {analysis['entrepreneur']} Works",
            entrepreneur=analysis['entrepreneur'],
            total_duration=target_duration * 60,
            sections=[],  # TODO: Parse sections
            full_script=script_text
        )
    
    def _founders_style_prompt(self) -> str:
        return """Write a podcast script in the style of FOUNDERS PODCAST (David Senra).

## VOICE & TONE
- Conversational, like talking to a friend
- PASSIONATE about the material
- Personal commentary: "Here's what I find fascinating..."
- Direct address: "Think about this for YOUR business..."
- Express genuine enthusiasm: "This is INSANE. Let me explain why..."
- Authentic reactions: "I couldn't believe this when I read it..."

## STRUCTURE

### 1. HOOK (30 seconds)
Start with the payoff. What will they learn?
Example: "This episode covers the insanely valuable company-building principles of [NAME]—and nothing else."

### 2. RESEARCH CONTEXT (1-2 minutes)
Build credibility. How deep did you go?
Example: "I spent 40 hours reading this 600-page biography. I took 50 pages of notes. Then I deleted everything that wasn't about how [NAME] actually builds companies."

### 3. PRINCIPLES (Main content, 35-40 minutes)
For each principle:
a) Set up the story
b) Tell the specific example
c) Read the key quote (dramatically)
d) Personal commentary on why it matters
e) Application for the listener

### 4. SYNTHESIS (3-5 minutes)
Pull it together:
- Key patterns across principles
- The one thing to remember
- Call to action

## LANGUAGE PATTERNS

Use these phrases naturally:
- "Let me read you this quote..."
- "Here's the crazy part..."
- "Think about what that means..."
- "This is the insight..."
- "Notice what he's doing here..."
- "The lesson for us is..."

## READING QUOTES
When reading quotes, set them up:
"Listen to how [NAME] puts this: [pause] [QUOTE]"
"Here's how he describes it: [pause] [QUOTE]"

## EMPHASIS
Mark emphasis with CAPS or *asterisks* for voice inflection:
"This is NOT about working harder. It's about working *differently*."
"""
    
    def _educational_style_prompt(self) -> str:
        return """Write an educational podcast script..."""
    
    def _storytelling_style_prompt(self) -> str:
        return """Write a narrative storytelling podcast script..."""
    
    def save_script(self, script: PodcastScript, output_path: str):
        """Save script to file."""
        with open(output_path, 'w') as f:
            f.write(script.full_script)
        
        # Also save metadata
        with open(output_path.replace('.txt', '_meta.json'), 'w') as f:
            json.dump({
                'title': script.title,
                'entrepreneur': script.entrepreneur,
                'duration': script.total_duration
            }, f, indent=2)


# Usage
if __name__ == "__main__":
    generator = ScriptGenerator()
    
    script = generator.generate_script(
        analysis_path="elon_analysis.json",
        target_duration=45,
        style="founders_podcast"
    )
    
    generator.save_script(script, "elon_script.txt")
```

---

## Module 3: Voice Generator

### Purpose
Convert script to audio using ElevenLabs.

### voice_generator.py

```python
"""
Voice Generator
Converts scripts to audio using ElevenLabs API.
"""

import os
from elevenlabs import generate, save, voices, Voice, VoiceSettings
from pathlib import Path
from typing import Optional
import json

class VoiceGenerator:
    def __init__(self, api_key: Optional[str] = None):
        if api_key:
            os.environ["ELEVEN_API_KEY"] = api_key
        
        self.default_voice_settings = VoiceSettings(
            stability=0.5,
            similarity_boost=0.75,
            style=0.5,
            use_speaker_boost=True
        )
    
    def list_voices(self):
        """List available voices."""
        return voices()
    
    def generate_audio(
        self,
        script_path: str,
        voice_id: str,
        output_path: str,
        model: str = "eleven_multilingual_v2"
    ) -> str:
        """Generate audio from script."""
        
        # Load script
        with open(script_path, 'r') as f:
            script_text = f.read()
        
        # For long scripts, chunk and generate
        if len(script_text) > 5000:
            return self._generate_long_audio(
                script_text, voice_id, output_path, model
            )
        
        # Generate audio
        audio = generate(
            text=script_text,
            voice=voice_id,
            model=model
        )
        
        # Save
        save(audio, output_path)
        return output_path
    
    def _generate_long_audio(
        self,
        script: str,
        voice_id: str,
        output_path: str,
        model: str
    ) -> str:
        """Handle long scripts by chunking."""
        from pydub import AudioSegment
        
        # Split by paragraphs, keeping under 5000 chars
        chunks = self._smart_chunk(script, max_chars=4500)
        
        audio_segments = []
        for i, chunk in enumerate(chunks):
            print(f"Generating chunk {i+1}/{len(chunks)}...")
            
            audio = generate(
                text=chunk,
                voice=voice_id,
                model=model
            )
            
            # Save temp file
            temp_path = f"/tmp/chunk_{i}.mp3"
            save(audio, temp_path)
            
            # Load as AudioSegment
            segment = AudioSegment.from_mp3(temp_path)
            audio_segments.append(segment)
        
        # Combine all segments
        combined = audio_segments[0]
        for segment in audio_segments[1:]:
            combined += segment
        
        # Export final audio
        combined.export(output_path, format="mp3")
        return output_path
    
    def _smart_chunk(self, text: str, max_chars: int = 4500) -> list:
        """Split text into chunks at natural break points."""
        chunks = []
        current_chunk = ""
        
        # Split by paragraphs
        paragraphs = text.split("\n\n")
        
        for para in paragraphs:
            if len(current_chunk) + len(para) < max_chars:
                current_chunk += para + "\n\n"
            else:
                if current_chunk:
                    chunks.append(current_chunk.strip())
                current_chunk = para + "\n\n"
        
        if current_chunk:
            chunks.append(current_chunk.strip())
        
        return chunks
    
    def clone_voice(self, name: str, audio_files: list) -> str:
        """Clone a voice from audio samples."""
        from elevenlabs import clone
        
        voice = clone(
            name=name,
            files=audio_files,
        )
        
        return voice.voice_id


# Usage
if __name__ == "__main__":
    generator = VoiceGenerator()
    
    # List available voices
    available = generator.list_voices()
    print(f"Available voices: {[v.name for v in available]}")
    
    # Generate audio
    generator.generate_audio(
        script_path="elon_script.txt",
        voice_id="pNInz6obpgDQGcFmaJgB",  # Adam voice
        output_path="elon_podcast.mp3"
    )
```

---

## Module 4: Video Creator

### Purpose
Create simple podcast-style video from audio.

### video_creator.py

```python
"""
Video Creator
Creates podcast-style videos with minimal visuals.
"""

from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont
import os
from typing import Optional, List
from dataclasses import dataclass

@dataclass
class VideoConfig:
    width: int = 1920
    height: int = 1080
    fps: int = 30
    background_color: tuple = (20, 20, 20)  # Dark gray
    text_color: tuple = (255, 255, 255)  # White
    accent_color: tuple = (255, 107, 107)  # Red accent

class VideoCreator:
    def __init__(self, config: Optional[VideoConfig] = None):
        self.config = config or VideoConfig()
    
    def create_podcast_video(
        self,
        audio_path: str,
        entrepreneur_image: str,
        title: str,
        output_path: str,
        quotes: Optional[List[str]] = None
    ) -> str:
        """Create a podcast-style video."""
        
        # Load audio
        audio = AudioFileClip(audio_path)
        duration = audio.duration
        
        # Create background
        bg = ColorClip(
            size=(self.config.width, self.config.height),
            color=self.config.background_color,
            duration=duration
        )
        
        # Add entrepreneur image (centered, slightly above middle)
        if os.path.exists(entrepreneur_image):
            img = ImageClip(entrepreneur_image)
            img = img.resize(height=600)
            img = img.set_position(("center", 150))
            img = img.set_duration(duration)
        else:
            img = None
        
        # Create title text
        title_txt = TextClip(
            title,
            fontsize=48,
            color='white',
            font='Arial-Bold',
            method='caption',
            size=(self.config.width - 200, None)
        )
        title_txt = title_txt.set_position(("center", 800))
        title_txt = title_txt.set_duration(duration)
        
        # Compose layers
        layers = [bg]
        if img:
            layers.append(img)
        layers.append(title_txt)
        
        # Add audio waveform visualization (optional)
        # TODO: Implement waveform
        
        # Composite
        video = CompositeVideoClip(layers)
        video = video.set_audio(audio)
        
        # Export
        video.write_videofile(
            output_path,
            fps=self.config.fps,
            codec='libx264',
            audio_codec='aac'
        )
        
        return output_path
    
    def create_thumbnail(
        self,
        entrepreneur_image: str,
        title: str,
        output_path: str
    ) -> str:
        """Create YouTube thumbnail."""
        
        # Create base image
        img = Image.new(
            'RGB',
            (1280, 720),
            color=(20, 20, 20)
        )
        draw = ImageDraw.Draw(img)
        
        # Add entrepreneur image
        if os.path.exists(entrepreneur_image):
            portrait = Image.open(entrepreneur_image)
            portrait = portrait.resize((400, 500))
            img.paste(portrait, (50, 110))
        
        # Add title text
        try:
            font = ImageFont.truetype("Arial-Bold.ttf", 72)
        except:
            font = ImageFont.load_default()
        
        # Word wrap title
        words = title.split()
        lines = []
        current_line = ""
        for word in words:
            if len(current_line + " " + word) < 20:
                current_line += " " + word
            else:
                lines.append(current_line.strip())
                current_line = word
        lines.append(current_line.strip())
        
        y = 200
        for line in lines:
            draw.text((500, y), line, fill=(255, 255, 255), font=font)
            y += 90
        
        # Save
        img.save(output_path)
        return output_path


# Usage
if __name__ == "__main__":
    creator = VideoCreator()
    
    # Create video
    creator.create_podcast_video(
        audio_path="elon_podcast.mp3",
        entrepreneur_image="elon_portrait.jpg",
        title="How Elon Musk Works\nCompany-Building Principles",
        output_path="elon_video.mp4"
    )
    
    # Create thumbnail
    creator.create_thumbnail(
        entrepreneur_image="elon_portrait.jpg",
        title="HOW ELON\nWORKS",
        output_path="elon_thumbnail.jpg"
    )
```

---

## Module 5: Pipeline Orchestrator

### Purpose
Orchestrate the full pipeline from book to published video.

### pipeline.py

```python
"""
Pipeline Orchestrator
End-to-end automation from book to YouTube.
"""

import os
import json
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
from datetime import datetime

from book_analyzer import BookAnalyzer
from script_generator import ScriptGenerator
from voice_generator import VoiceGenerator
from video_creator import VideoCreator

@dataclass
class PipelineConfig:
    output_dir: str = "./output"
    voice_id: str = "pNInz6obpgDQGcFmaJgB"  # Default ElevenLabs voice
    target_duration: int = 45  # minutes
    style: str = "founders_podcast"

class ContentPipeline:
    def __init__(self, config: Optional[PipelineConfig] = None):
        self.config = config or PipelineConfig()
        
        self.book_analyzer = BookAnalyzer()
        self.script_generator = ScriptGenerator()
        self.voice_generator = VoiceGenerator()
        self.video_creator = VideoCreator()
        
        # Create output directory
        Path(self.config.output_dir).mkdir(parents=True, exist_ok=True)
    
    def run(
        self,
        book_path: str,
        entrepreneur: str,
        book_title: str,
        author: str,
        portrait_image: str
    ) -> dict:
        """Run full pipeline."""
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        project_dir = Path(self.config.output_dir) / f"{entrepreneur.lower().replace(' ', '_')}_{timestamp}"
        project_dir.mkdir(parents=True, exist_ok=True)
        
        results = {
            "entrepreneur": entrepreneur,
            "book_title": book_title,
            "timestamp": timestamp,
            "steps": {}
        }
        
        # Step 1: Analyze book
        print(f"📚 Step 1/5: Analyzing book...")
        book_text = self.book_analyzer.extract_text_from_pdf(book_path)
        analysis = self.book_analyzer.analyze_book(
            book_text, entrepreneur, book_title, author
        )
        analysis_path = project_dir / "analysis.json"
        self.book_analyzer.save_analysis(analysis, str(analysis_path))
        results["steps"]["analysis"] = str(analysis_path)
        print(f"   ✅ Analysis saved to {analysis_path}")
        
        # Step 2: Generate script
        print(f"✍️  Step 2/5: Generating script...")
        script = self.script_generator.generate_script(
            str(analysis_path),
            self.config.target_duration,
            self.config.style
        )
        script_path = project_dir / "script.txt"
        self.script_generator.save_script(script, str(script_path))
        results["steps"]["script"] = str(script_path)
        print(f"   ✅ Script saved to {script_path}")
        
        # Step 3: Generate audio
        print(f"🎙️  Step 3/5: Generating audio...")
        audio_path = project_dir / "podcast.mp3"
        self.voice_generator.generate_audio(
            str(script_path),
            self.config.voice_id,
            str(audio_path)
        )
        results["steps"]["audio"] = str(audio_path)
        print(f"   ✅ Audio saved to {audio_path}")
        
        # Step 4: Create video
        print(f"🎬 Step 4/5: Creating video...")
        video_path = project_dir / "video.mp4"
        self.video_creator.create_podcast_video(
            str(audio_path),
            portrait_image,
            f"How {entrepreneur} Works",
            str(video_path)
        )
        results["steps"]["video"] = str(video_path)
        print(f"   ✅ Video saved to {video_path}")
        
        # Step 5: Create thumbnail
        print(f"🖼️  Step 5/5: Creating thumbnail...")
        thumbnail_path = project_dir / "thumbnail.jpg"
        self.video_creator.create_thumbnail(
            portrait_image,
            f"HOW {entrepreneur.upper()}\nWORKS",
            str(thumbnail_path)
        )
        results["steps"]["thumbnail"] = str(thumbnail_path)
        print(f"   ✅ Thumbnail saved to {thumbnail_path}")
        
        # Save results
        results_path = project_dir / "pipeline_results.json"
        with open(results_path, 'w') as f:
            json.dump(results, f, indent=2)
        
        print(f"\n🎉 Pipeline complete! All files in: {project_dir}")
        return results


# CLI interface
if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="YouTube Content Pipeline")
    parser.add_argument("--book", required=True, help="Path to book PDF")
    parser.add_argument("--entrepreneur", required=True, help="Entrepreneur name")
    parser.add_argument("--title", required=True, help="Book title")
    parser.add_argument("--author", required=True, help="Book author")
    parser.add_argument("--portrait", required=True, help="Path to portrait image")
    parser.add_argument("--output", default="./output", help="Output directory")
    parser.add_argument("--voice", default="pNInz6obpgDQGcFmaJgB", help="ElevenLabs voice ID")
    parser.add_argument("--duration", type=int, default=45, help="Target duration in minutes")
    
    args = parser.parse_args()
    
    config = PipelineConfig(
        output_dir=args.output,
        voice_id=args.voice,
        target_duration=args.duration
    )
    
    pipeline = ContentPipeline(config)
    pipeline.run(
        book_path=args.book,
        entrepreneur=args.entrepreneur,
        book_title=args.title,
        author=args.author,
        portrait_image=args.portrait
    )
```

---

## Setup Instructions

### 1. Install Dependencies

```bash
pip install anthropic openai elevenlabs moviepy Pillow PyPDF2 pydub
```

### 2. Set Environment Variables

```bash
export ANTHROPIC_API_KEY=your_anthropic_key
export ELEVEN_API_KEY=your_elevenlabs_key
```

### 3. Run Pipeline

```bash
python pipeline.py \
    --book "elon_musk_biography.pdf" \
    --entrepreneur "Elon Musk" \
    --title "Elon Musk" \
    --author "Walter Isaacson" \
    --portrait "elon_portrait.jpg" \
    --duration 45
```

---

## Cost Estimate

| Service | Usage | Cost |
|---------|-------|------|
| Claude API | ~200K tokens/book | ~$3 |
| ElevenLabs | ~50K characters/video | ~$5 |
| Total per video | | **~$8** |

At 4 videos/month = ~$32/month

---

## Next Steps

1. **Test each module independently**
2. **Run full pipeline on test book**
3. **Iterate on script quality**
4. **Create custom voice clone**
5. **Add YouTube upload automation**
