print('Testando...')

import speech_recognition as sr
import os

def listen_microphone():
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        microphone.adjust_for_ambient_noise(source)

        print('Diga alguma coisa: ')

        audio = microphone.listen(source)

    try:
        phrase = microphone.recognize_google(audio, language='pt-BR')

        if 'navegador' in phrase:
            os.system('start Chrome.exe')

        elif 'Excel' in phrase:
            os.system('start Excel.exe')

        print('Você disse: ' + phrase)

    except sr.UnkownValueError:
        print('Não entendi!')

    return phrase

listen_microphone()
