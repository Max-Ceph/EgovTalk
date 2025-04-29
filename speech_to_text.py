from google.cloud import speech
import io
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "credentials/egovtalk-key.json"

def recognize_speech(audio_path):
    client = speech.SpeechClient()

    with io.open(audio_path, "rb") as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=48000,  # частота wav файла
        language_code="ru-RU"
    )

    response = client.recognize(config=config, audio=audio)

    text = ""
    for result in response.results:
        text += result.alternatives[0].transcript + " "

    return text.strip() if text else None
