import speech_recognition as sr
import os
import time 
import sys

def print_typing(textus, delay=0.1):
    for char in textus:
        sys.stdout.write(char)  
        sys.stdout.flush()      
        time.sleep(delay)        
    print()

recognizer = sr.Recognizer()
while True:            
    provodnik = "::{20D04FE0-3AEA-1069-A2D8-08002B30309D}"
    chrome = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
    
    with sr.Microphone() as source:
        print("Скажите что-нибудь:")
        audio = recognizer.listen(source)
        
    try:
        text = recognizer.recognize_google(audio, language="ru-RU")
        text1 = text.lower()
        print('вы сказали: ' + text1)
        
        if text1 == 'открой проводник':
            os.startfile(provodnik)
        elif text1 == 'открой chrome' or text1 == 'открой гугл' or text1 == 'открой браузер':
            os.startfile(chrome)
        
        if 'пиши под диктовку' in text1:
            phrase = 'пиши под диктовку'
            middle_index = text1[text1.index(phrase) + len(phrase):].strip()
            print('Всегда готов!')
            print_typing(middle_index)
        
    except sr.UnknownValueError:
        print("Не удалось распознать речь")
    except sr.RequestError as e:
        print(f"Ошибка сервиса распознавания: {e}")
