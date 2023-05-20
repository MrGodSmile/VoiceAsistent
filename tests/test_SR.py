import deepspeech
import numpy as np
import pyaudio
import wave
import tensorflow as tf

# Загрузка модели из файла ckpt
loaded = tf.saved_model.load(r'C:\Users\mrgod\PycharmProjects\librispeech_pretrained_v3.ckpt')

# Преобразование в формат mmapped
tf.saved_model.save(loaded, r'C:\Users\mrgod\PycharmProjects\librispeech_pretrained_v3.mmapped')
# Путь к предварительно обученной модели DeepSpeech
model_path = r'C:\Users\mrgod\PycharmProjects\librispeech_pretrained_v3.ckpt'
# Путь к файлу алфавита
alphabet_path = r'C:\Users\mrgod\PycharmProjects\alphabet.txt'

# Создание экземпляра модели DeepSpeech и загрузка параметров модели
model = deepspeech.Model(model_path)
model.set_alphabet(alphabet_path)

# Настройки захвата аудио с микрофона
sample_rate = 16000
chunk_size = 1024

audio = pyaudio.PyAudio()
stream = audio.open(format=pyaudio.paInt16, channels=1, rate=sample_rate, input=True, frames_per_buffer=chunk_size)

# Функция для распознавания речи с микрофона
def recognize_speech():
    frames = []

    while True:
        data = stream.read(chunk_size)
        frames.append(data)
        audio_data = np.frombuffer(data, dtype=np.int16)

        # Остановка записи, если уровень звука ниже заданного порога (например, если пользователь перестал говорить)
        if np.abs(audio_data).mean() < 500:
            break

    audio_data = np.hstack(frames)
    text = model.stt(audio_data)

    return text

# Вызов функции recognize_speech() для распознавания речи с микрофона
recognized_text = recognize_speech()
print(recognized_text)