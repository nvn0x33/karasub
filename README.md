# Karasub

Karasub is a Python tool that creates karaoke-style subtitles from a video. It transcribes the audio, generates an `.ass` subtitle file, and can burn those subtitles into the video.

## Features

-   Extract audio from a video
-   Generate karaoke-style `.ass` subtitles
-   Burn subtitles into the video
-   Simple to run and easy to modify

## Installation

```bash
git clone https://github.com/nvn0x33/karasub.git
cd Karasub
pip install -r requirements.txt
```

## Usage

```bash
python main.py
```

## Note

The subtitle generation is working as intended, and the generated `.ass` are working correctly in Aegisub.

The video rendering step is still a work in progress. In some videos, the burned subtitles may overlap or not render exactly as expected. If you only need the subtitle file, it should work perfectly with any player or editor that supports the ASS format.

I'm planning to improve the rendering pipeline in future updates.
