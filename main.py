import time
from plyer import notification
from moviepy.editor import *
from moviepy.config import change_settings
from moviepy.editor import concatenate_videoclips, VideoFileClip
import SilenceCutter as Sc
import Transcriber as Tc

IMAGEMAGICK_PATH = r"C:\Program Files\ImageMagick-7.1.1-Q16-HDRI\magick.exe"
change_settings({"IMAGEMAGICK_BINARY": IMAGEMAGICK_PATH})

backGroundClip = VideoFileClip("Background.mp4")
backGroundClip = backGroundClip.without_audio()
backGroundClip = backGroundClip.subclip(0, 60)


def generate_subtitles():
    audio_transcription = Tc.transcribe()
    start = time.time()
    segment_index = 0
    word_index = 0
    captions = []
    while True:
        words = audio_transcription["segments"][segment_index]["words"]
        current_time = (time.time() - start)
        word_start = words[word_index]["start"]
        current_word = words[word_index]["text"]
        word_duration = words[word_index]["end"] - words[word_index]["start"]
        if current_time > word_start:
            txt_clip = TextClip(current_word.upper().replace(".", "").replace(".", ""), fontsize=150, color="white",
                                stroke_color="black", stroke_width=5.5, font="Impact")
            txt_clip = txt_clip.set_pos('center').set_duration(word_duration)
            captions.append(txt_clip)
            if word_index + 1 < len(words):
                word_index += 1
            else:
                if segment_index + 1 < len(audio_transcription["segments"]):
                    word_index = 0
                    segment_index += 1
                else:
                    break
    return captions


subtitles = generate_subtitles()

subtitle_clip = concatenate_videoclips(subtitles, method="compose").set_position(("center", "center"))
Sc.remove_silence()

audio_clip = AudioFileClip("facts.mp3")

video = CompositeVideoClip([backGroundClip, subtitle_clip])
video = video.set_audio(audio_clip)
video.ipython_display(width=280)

notification.notify(
    title='Video Generated',
    message='the video has been generated!',
    app_icon=None,
    timeout=10,
)
