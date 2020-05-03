# EV3
from ev3dev2.button import Button

class BrickButton:
    Button = None
    ButtonDownCallbackFunc = None
    ButtonDownCallbackArgs = dict()
    ButtonEnterCallbackFunc = None
    ButtonEnterCallbackArgs = dict()
    ButtonLeftCallbackFunc = None
    ButtonLeftCallbackArgs = dict()
    ButtonRightCallbackFunc = None
    ButtonRightCallbackArgs = dict()
    ButtonUpCallbackFunc = None
    ButtonUpCallbackArgs = dict()

    #
    # Init
    # Initialize the brick buttons
    def __init__(self):
        self.Button = Button()

        self.Button.on_down = self.__ButtonDown
        self.Button.on_enter = self.__ButtonEnter
        self.Button.on_left = self.__ButtonLeft
        self.Button.on_right = self.__ButtonRight
        self.Button.on_up = self.__ButtonUp

    #
    # ButtonDown
    # Private method associated with the brick down button
    def __ButtonDown(self, State):
        while self.Button.down:
            print('Down button pressed')
            if self.ButtonDownCallbackFunc is not None:
                self.ButtonDownCallbackFunc(**self.ButtonDownCallbackArgs)

    #
    # ButtonEnter
    # Private method associated with the brick enter button
    def __ButtonEnter(self, State):
        while self.Button.enter:
            print('Enter button pressed')
            if self.ButtonEnterCallbackFunc is not None:
                self.ButtonEnterCallbackFunc(**self.ButtonEnterCallbackArgs)

    #
    # ButtonLeft
    # Private method associated with the brick left button
    def __ButtonLeft(self, State):
        while self.Button.left:
            print('Left button pressed')
            if self.ButtonLeftCallbackFunc is not None:
                self.ButtonLeftCallbackFunc(**self.ButtonLeftCallbackArgs)
    
    #
    # ButtonRight
    # Private method associated with the brick right button
    def __ButtonRight(self, State):
        while self.Button.right:
            print('Right button pressed')
            if self.ButtonRightCallbackFunc is not None:
                self.ButtonRightCallbackFunc(**self.ButtonRightCallbackArgs)

    #
    # ButtonUp
    # Private method associated with the brick up button
    def __ButtonUp(self, State):
        while self.Button.up:
            print('Up button pressed')
            if self.ButtonUpCallbackFunc is not None:
               self.ButtonUpCallbackFunc(**self.ButtonUpCallbackArgs)
