# Python Imports
from requests import get as GetAPI

# Cube faces:
# U = Up, L = Left, F = Front, R = Right, B = Back, D = Down
#
#            UU UU UU
#            UU UU UU
#            UU UU UU
#  LL LL LL  FF FF FF  RR RR RR  BB BB BB
#  LL LL LL  FF FF FF  RR RR RR  BB BB BB
#  LL LL LL  FF FF FF  RR RR RR  BB BB BB
#            DD DD DD
#            DD DD DD
#            DD DD DD
#
# Square indexes:
#            01 02 03
#            04 05 06
#            07 08 09
#  10 11 12  19 20 21  28 29 30  37 38 39
#  13 14 15  22 23 24  31 32 33  40 41 42
#  16 17 18  25 26 27  34 35 36  43 44 45
#            46 47 48
#            49 50 51
#            52 53 54 

class Square:
    __BaseColors = {
        'Bl': (0.00, 0.00, 0.00), # Black
        'Bu': (32.0426042551867, 12.950151429585361, -45.17310190169409), # Blue
        'Gr': (49.32919074877404, 3.645985298946497, -48.7013011581894), # Green
        'Or': (91.1398835176748, -22.214881513032246, -13.748361790456599), # Orange
        'Rd': (20.336797974719104, 34.63161034632639, 8.618994602944529), # Red
        'Wh': (99.99998453333127, -0.0004593894083471106, -0.008561457924405325), # White
        'Ye': (91.65285503582525, -8.473773852420429, -12.761759278634809) # Yellow
    }
    __LABColor = None

    _Blue = 0
    _ColorName = None
    _Green = 0
    _Position = 0
    _Red = 0
    _Type = None

    def __init__(self):
        return

    ######################
    # Properties Methods #
    ######################
    #
    # Blue property
    @property
    def Blue(self):
        return self._Blue

    @Blue.setter
    def Blue(self, Blue):
        if not isinstance(Blue, int):
            raise ValueError('Not integer Blue is not possible')

        self._Blue = Blue

    @Blue.deleter
    def Blue(self):
        del self._Blue

    #
    # ColorName property
    @property
    def ColorName(self):
        return self._ColorName

    @ColorName.setter
    def ColorName(self, Name):
        if not isinstance(Name, str):
            raise ValueError('Not string ColorName is not possible')

        self._ColorName = Name

    @ColorName.deleter
    def ColorName(self):
        del self._ColorName

    #
    # Green property
    @property
    def Green(self):
        return self._Green

    @Green.setter
    def Green(self, Green):
        if not isinstance(Green, int):
            raise ValueError('Not integer Green is not possible')

        self._Green = Green

    @Green.deleter
    def Green(self):
        del self._Green

    #
    # Position property
    @property
    def Position(self):
        return self._Position

    @Position.setter
    def Position(self, Position):
        if not isinstance(Position, int):
            raise ValueError('Not integer Position is not possible')

        self._Position = Position

    @Position.deleter
    def Position(self):
        del self._Position

    #
    # Red property
    @property
    def Red(self):
        return self._Red

    @Red.setter
    def Red(self, Red):
        if not isinstance(Red, int):
            raise ValueError('Not integer Red is not possible')

        self._Red = Red

    @Red.deleter
    def Red(self):
        del self._Red

    #
    # Type property
    @property
    def Type(self):
        return self._Type

    @Type.setter
    def Type(self, Type):
        if not isinstance(Type, str):
            raise ValueError('Not string Type is not possible')
        if Type not in [ 'C', 'E', 'M' ]:
            raise ValueError('Type "{}" unknown, use one of: C for Corner, E for Edge, M for Middle')

        self._Type = Type

    @Type.deleter
    def Type(self):
        del self._Type

    ###################
    # Exposed Methods #
    ###################
    #
    # FindColor
    # Retrieve the color related to the Red, Green and Blue rgb color codes
    def FindColor(self):
        CieData = []
    
        if self.__LABColor is None:
            self.__RgbToLab()

        for (ColorShortName, LABColorCode) in self.__BaseColors.items():
            APIResponse = GetAPI(
                'http://192.168.85.13:5000/bots-api/cube-solver/labs-distance',
                data = {
                    'lab1_lightness': self.__LABColor[0],
                    'lab1_dim_a': self.__LABColor[1],
                    'lab1_dim_b': self.__LABColor[2],
                    'lab2_lightness': LABColorCode[0],
                    'lab2_dim_a': LABColorCode[1],
                    'lab2_dim_b': LABColorCode[2]
                }
            )
            if APIResponse.status_code == 200:
                CieData.append(
                    (
                        APIResponse.json()['Distance'],
                        ColorShortName
                    )
                )

        CieData = sorted(CieData)

        if len(CieData) > 0:
            self._ColorName = CieData[0][1]

    ###################
    # Private Methods #
    ###################
    #
    # RgbToLab
    # Convert rgb color code to a tuple of a lab color code
    def __RgbToLab(self):
        APIResponse = GetAPI(
            'http://192.168.85.13:5000/bots-api/cube-solver/rgb-to-lab',
            data = {
                'red': self.Red,
                'green': self.Green,
                'blue': self.Blue
            }
        )
        if APIResponse.status_code == 200:
            LABJson = APIResponse.json()
            self.__LABColor = (
                LABJson['Lab']['L'],
                LABJson['Lab']['A'],
                LABJson['Lab']['B']
            )
        else:
            return None