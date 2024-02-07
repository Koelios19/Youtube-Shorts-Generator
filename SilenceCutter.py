from pydub import AudioSegment
from pydub.silence import split_on_silence
from plyer import notification

def remove_silence():
    file_path = "facts.mp3"
    file_name = file_path.split('/')[-1]
    audio_format = "mp3"
    # Reading and splitting the audio file into chunks
    sound = AudioSegment.from_file(file_path, format=audio_format)
    audio_chunks = split_on_silence(sound
                                    , min_silence_len=800
                                    , silence_thresh=-35
                                    , keep_silence=False
                                    )
    # Putting the file back together
    combined = AudioSegment.empty()
    for chunk in audio_chunks:
        combined += chunk
    combined.export(f'{file_name}', format=audio_format)
