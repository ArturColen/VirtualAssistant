print('Testando...')

import speech_recognition as sr
import os

# Hear and recognize speech
def listen_microphone():
    microphone = sr.Recognizer()

    with sr.Microphone() as source:
        # Call an algorithm for noise reduction in sound
        microphone.adjust_for_ambient_noise(source)

        print('Diga alguma coisa: ')

        audio = microphone.listen(source)

    try:
        # Pass the variable to the pattern recognition algorithm
        phrase = microphone.recognize_google(audio, language='pt-BR')

        if 'navegador' in phrase:
            os.system('start Chrome.exe')

        elif 'Excel' in phrase:
            os.system('start Excel.exe')

        # Return the phrase pronounced
        print('Você disse: ' + phrase)

    # Phrase to be displayed if it does not recognize the speech pattern
    except sr.UnkownValueError:
        print('Não entendi!')

    return phrase

listen_microphone()
