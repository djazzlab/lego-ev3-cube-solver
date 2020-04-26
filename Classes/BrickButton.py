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
        if State:
            print('Down button pressed')
            if self.ButtonDownCallbackFunc is not None:
                self.ButtonDownCallbackFunc(**self.ButtonDownCallbackArgs)
        else:
            print('Down button released')

    #
    # ButtonEnter
    # Private method associated with the brick enter button
    def __ButtonEnter(self, State):
        if State:
            print('Enter button pressed')
            if self.ButtonEnterCallbackFunc is not None:
                self.ButtonEnterCallbackFunc(**self.ButtonEnterCallbackArgs)
        else:
            print('Enter button released')

    #
    # ButtonLeft
    # Private method associated with the brick left button
    def __ButtonLeft(self, State):
        if State:
            print('Left button pressed')
            if self.ButtonLeftCallbackFunc is not None:
                self.ButtonLeftCallbackFunc(**self.ButtonLeftCallbackArgs)
        else:
            print('Left button released')
    
    #
    # ButtonRight
    # Private method associated with the brick right button
    def __ButtonRight(self, State):
        if State:
            print('Right button pressed')
            if self.ButtonRightCallbackFunc is not None:
                self.ButtonRightCallbackFunc(**self.ButtonRightCallbackArgs)
        else:
            print('Right button released')

    #
    # ButtonUp
    # Private method associated with the brick up button
    def __ButtonUp(self, State):
        if State:
            print('Up button pressed')
            if self.ButtonUpCallbackFunc is not None:
               self.ButtonUpCallbackFunc(**self.ButtonUpCallbackArgs)
        else:
            print('Up button released')