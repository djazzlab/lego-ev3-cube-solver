from ev3dev2.sound import Sound

class BrickVoice:
    Voice = None

    def __init__(self):
        self.Voice = Sound()

    def Speak(self, Message):
        self.Voice.speak(Message)