# Colormath Package
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_diff import delta_e_cie2000 as DeltaCie2000
from colormath.color_conversions import convert_color as ConvertColor

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
        'Rd': (42.55, 65.36, 50.70), # Red
        'Or': (51.91, 51.79, 60.30), # Red Orange
        'OR': (67.05, 42.83, 74.03), # Orange
        'Ye': (91.29, -15.30, 86.36), # Yellow
        'Yg': (69.71, -59.25, 69.14), # Yellow Green
        'Gr': (51.41, -52.75, 51.85), # Green
        'Sy': (73.88, -24.30, -34.55), # Sky Blue
        'Bu': (42.29, 12.80, -51.30), # Blue
        'Pu': (41.53, 48.15, -53.96), # Purple
        'Wh': (100.00, 0.01, -0.01), # White
        'Bl': (0.00, 0.00, 0.00)  # Black
    }

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

        for (ColorShortName, LABColorCode) in self.__BaseColors.iteritems():
            Distance = DeltaCie2000(self.__RgbToLab(), LABColorCode)
            CieData.append((Distance, ColorShortName))
        CieData = sorted(CieData)

        if len(CieData) > 0:
            self._ColorName = CieData[0][1]
        
        return self._ColorName

    ###################
    # Private Methods #
    ###################
    #
    # RgbToLab
    # Convert Rgb color code to lab color code
    def __RgbToLab(self):
        return ConvertColor(
            sRGBColor(self.Red, self.Green, self.Blue, True),
            LabColor
        )