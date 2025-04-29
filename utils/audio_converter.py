from pydub import AudioSegment

def convert_ogg_to_wav(source_path, target_path):
    audio = AudioSegment.from_file(source_path, format="ogg")
    audio = audio.set_frame_rate(48000)
    audio = audio.set_sample_width(2)
    audio = audio.set_channels(1)
    audio.export(target_path, format="wav")