# Youtube-Shorts-Generator
This project was done as an 48h-hour challenge as in my [recent video](https://youtu.be/ZmSb3LZDdf0](https://www.youtube.com/watch?v=HWuVNHEnr1A)https://www.youtube.com/watch?v=HWuVNHEnr1A).

*Its sole purpose is to automate the process of creating youtube shorts by generating a number of random fun facts that can be spoken within 60 seconds by a TTS model, displayed on top of a satisfying background with accompanying synced subtitles.*

---

## Installation:
- Install dependencies.
- Download this [mp3 file](). Move it to the same folder and make sure it's named `background.mp3`
- Grab an Eleven Labs API key from [here](https://elevenlabs.io/api) and set it to `api_key` (line 4 in `FactTeller.py`).
  
Now run `python main.py` and wait. The program takes roughly 3 minutes and the output will be saved as `__temp__.mp4`.
