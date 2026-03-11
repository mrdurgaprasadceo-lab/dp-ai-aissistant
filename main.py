import os
import eel

from engine.features import *
from engine.command import *
from engine.auth import recoganize
from engine.command import runAssistant


def start():

    eel.init("www")

    playAssistantSound()

    @eel.expose
    def init():
        eel.hideLoader()
        speak("Ready for Face Authentication")

        flag = 1

        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can I Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")

    init()

    runAssistant()

    eel.start('index.html', size=(1200,700))


if __name__ == "__main__":
    start()