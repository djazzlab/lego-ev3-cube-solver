# Cube Classes
from Classes.Rubik.Square import Square

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

class Face:
    __FaceIndexes = {
        'U': 0,
        'L': 1,
        'F': 2,
        'R': 3,
        'B': 4,
        'D': 5
    }
    __FaceSquares = None

    _CornerSquarePositions = None
    _EdgeSquarePositions = None
    _GreaterSquarePosition = 0
    _LesserSquarePosition = 0
    _MiddleSquarePosition = 0
    _Name = None

    def __init__(self, Name):
        self.__FaceSquares = []
        self._Name = Name

    ######################
    # Properties Methods #
    ######################
    #
    # CornerSquarePositions property
    @property
    def CornerSquarePositions(self):
        return self._CornerSquarePositions

    @CornerSquarePositions.setter
    def CornerSquarePositions(self, CornerSquarePositions):
        if not isinstance(CornerSquarePositions, tuple):
            raise ValueError('Not tuple CornerSquarePositions is not possible')

        self._CornerSquarePositions = CornerSquarePositions

    @CornerSquarePositions.deleter
    def CornerSquarePositions(self):
        del self._CornerSquarePositions

    #
    # EdgeSquarePositions property
    @property
    def EdgeSquarePositions(self):
        return self._EdgeSquarePositions

    @EdgeSquarePositions.setter
    def EdgeSquarePositions(self, EdgeSquarePositions):
        if not isinstance(EdgeSquarePositions, tuple):
            raise ValueError('Not tuple EdgeSquarePositions is not possible')

        self._EdgeSquarePositions = EdgeSquarePositions

    @EdgeSquarePositions.deleter
    def EdgeSquarePositions(self):
        del self._EdgeSquarePositions

    #
    # GreaterSquarePosition property
    @property
    def GreaterSquarePosition(self):
        return self._GreaterSquarePosition

    @GreaterSquarePosition.setter
    def GreaterSquarePosition(self, GreaterSquarePosition):
        if not isinstance(GreaterSquarePosition, int):
            raise ValueError('Not integer GreaterSquarePosition is not possible')

        self._GreaterSquarePosition = GreaterSquarePosition

    @GreaterSquarePosition.deleter
    def GreaterSquarePosition(self):
        del self._GreaterSquarePosition

    #
    # LesserSquarePosition property
    @property
    def LesserSquarePosition(self):
        return self._LesserSquarePosition

    @LesserSquarePosition.setter
    def LesserSquarePosition(self, LesserSquarePosition):
        if not isinstance(LesserSquarePosition, int):
            raise ValueError('Not integer LesserSquarePosition is not possible')

        self._LesserSquarePosition = LesserSquarePosition

    @LesserSquarePosition.deleter
    def LesserSquarePosition(self):
        del self._LesserSquarePosition

    #
    # MiddleSquarePosition property
    @property
    def MiddleSquarePosition(self):
        return self._MiddleSquarePosition

    @MiddleSquarePosition.setter
    def MiddleSquarePosition(self, MiddleSquarePosition):
        if not isinstance(MiddleSquarePosition, int):
            raise ValueError('Not integer MiddleSquarePosition is not possible')

        self._MiddleSquarePosition = MiddleSquarePosition

    @MiddleSquarePosition.deleter
    def MiddleSquarePosition(self):
        del self._MiddleSquarePosition

    #
    # Name property
    @property
    def Name(self):
        return self._Name
    
    @Name.setter
    def Name(self, Name):
        if not isinstance(Name, str):
            raise ValueError('Not string Name is not possible')
        if Name not in self.__FaceIndexes.keys():
            raise ValueError('Name "{}" is not known, use one of {}'.format(
                Name,
                self.__FaceIndexes.keys()
            ))

        self._Name = Name

    @Name.deleter
    def Name(self):
        del self._Name

    ###################
    # Exposed Methods #
    ###################
    #
    # GetFaceSquares
    # Returns a list of squares
    def GetFaceSquares(self):
        return self.__FaceSquares

    #
    # GetMiddleSquare
    # Returns the middle square of the face
    def GetMiddleSquare(self):
        for FaceSquare in self.__FaceSquares:
            if FaceSquare.Type == 'M':
                return FaceSquare
        return None

    #
    # GetSquareFromPosition
    # Retrieve face square from position
    def GetSquareFromPosition(Position):
        for FaceSquare in self.__FaceSquares:
            if FaceSquare.Position == Position:
                return FaceSquare
        return None

    #
    # RegisterSquare
    # Register a square definition (position and rgb color code) to the face
    def RegisterSquare(self, Position, Red, Green, Blue):
        print('Registering square "{}:{}"'.format(
            Position,
            (Red, Green, Blue)
        ))
        FaceSquare = Square()

        FaceSquare.Position = Position
        FaceSquare.Red = Red
        FaceSquare.Green = Green
        FaceSquare.Blue = Blue

        FaceSquare.FindColor()

        if Position == self._MiddleSquarePosition:
            FaceSquare.Type = 'M'
        elif Position in self._EdgeSquarePositions:
            FaceSquare.Type = 'E'
        else:
            FaceSquare.Type = 'C'

        self.__FaceSquares.append(FaceSquare)

    ###################
    # Private Methods #
    ###################
    #
    # ConfigureFace
    # Configure the square position of the face
    def __ConfigureFace(self):
        self._LesserSquarePosition = self.__FaceIndexes[self._Name] * 9 + 1
        self._GreaterSquarePosition = self.__FaceIndexes[self._Name] * 9 + 9
        self._MiddleSquarePosition = (self._LesserSquarePosition + self._GreaterSquarePosition) / 2
        self._EdgeSquarePositions = (
            self._LesserSquarePosition + 1,
            self._LesserSquarePosition + 3,
            self._LesserSquarePosition + 5,
            self._LesserSquarePosition + 7
        )
        self.CornerSquarePositions = (
            self._LesserSquarePosition,
            self._LesserSquarePosition + 2,
            self._LesserSquarePosition + 6,
            self._LesserSquarePosition + 8
        )