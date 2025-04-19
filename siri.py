import speech_recognition as sr
import os
recognizer = sr.Recognizer()
while True:
    provodnik = "C:"
    provo = 'бот открой проводник'
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        text1 = text.lower()
        print('вы сказали: ' + text1)
        if text1 == provo:
            os.startfile(provodnik)

    except sr.UnknownValueError:
        print("Не удалось распознать речь")

    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания: {e}")

