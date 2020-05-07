# Cube Classes
from Classes.Rubik.Corner import Corner
from Classes.Rubik.Edge import Edge
from Classes.Rubik.Face import Face

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

class Cube:
    __BaseColors = {
        'Bl': (0.00, 0.00, 0.00), # Black
        'Bu': (32.0426042551867, 12.950151429585361, -45.17310190169409), # Blue
        'Gr': (49.32919074877404, 3.645985298946497, -48.7013011581894), # Green
        'Or': (91.1398835176748, -22.214881513032246, -13.748361790456599), # Orange
        'Rd': (20.336797974719104, 34.63161034632639, 8.618994602944529), # Red
        'Wh': (99.99998453333127, -0.0004593894083471106, -0.008561457924405325), # White
        'Ye': (91.65285503582525, -8.473773852420429, -12.761759278634809) # Yellow
    }
    __Corners = None
    __Edges = None
    __Faces = {}

    def __init__(self):
        self.__Corners = []
        self.__Edges = []
        self.__Faces = {
            'U': Face(Name = 'U'),
            'L': Face(Name = 'L'),
            'F': Face(Name = 'F'),
            'R': Face(Name = 'R'),
            'B': Face(Name = 'B'),
            'D': Face(Name = 'D')
        }
    
    ###################
    # Exposed Methods #
    ###################
    #
    # ImportScannedData
    # Import scanned data to the cube object
    def ImportScannedData(self, ScannedData):
        APIResponse = GetAPI(
            'http://192.168.85.13:5000/bots-api/cube-solver/colors-from-json',
            json = {
                'base_colors': self.__BaseColors,
                'scanned_colors': ScannedData
            }
        )
        if APIResponse.status_code != 200:
            return None
        else:
            ColorNames = APIResponse.json()['Result']

        for (SquarePosition, (RedCode, GreenCode, BlueCode)) in ScannedData.items():
            Face = self.__FindCubeFaceFromSquarePosition(SquarePosition = SquarePosition)
            self.__Faces[Face.Name].RegisterSquare(
                Position = SquarePosition,
                Red = RedCode,
                Green = GreenCode,
                Blue = BlueCode,
                ColorName = ColorNames[str(SquarePosition)]
            )

        print(self.__Faces)

        self.__DefineCubeCorners()
        self.__DefineCubeEdges()

    #
    # PrintCube
    # Print the cube in the logs
    def PrintCube(self):
        Data = [ [], [], [], [], [], [], [], [], [] ]

        for CubeFace in self.__Faces:
            Prefix = ''
            if CubeFace.Name == 'U':
                Line = 0
                Prefix = '          '
            elif CubeFace.Name == 'D':
                Line = 6
                Prefix = '          '
            else:
                Line = 3

            for Index in xrange(3):
                Data[Line].append(Prefix)
                Data[Line].append('%2s' % CubeFace.GetSquareFromPosition(Position = CubeFace.LesserSquarePosition + (Index * 3)).ColorName)
                Data[Line].append('%2s' % CubeFace.GetSquareFromPosition(Position = CubeFace.LesserSquarePosition + 1 + (Index * 3)).ColorName)
                Data[Line].append('%2s' % CubeFace.GetSquareFromPosition(Position = CubeFace.LesserSquarePosition + 2 + (Index * 3)).ColorName)
                Line += 1

        Output = []
        for Row in Data:
            Output.append(' '.join(Row))

        print('%s' % '\n'.join(Output))

    ###################
    # Private Methods #
    ###################
    #
    # DefineCubeCorners
    # Define the corners of the cube for all faces
    def __DefineCubeCorners(self):
        # U
        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 1
        CubeCorner.SquarePosition2 = 10
        CubeCorner.SquarePosition3 = 39
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 3
        CubeCorner.SquarePosition2 = 37
        CubeCorner.SquarePosition3 = 30
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 7
        CubeCorner.SquarePosition2 = 19
        CubeCorner.SquarePosition3 = 12
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 9
        CubeCorner.SquarePosition2 = 28
        CubeCorner.SquarePosition3 = 21
        self.__Corners.append(CubeCorner)

        # B
        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 46
        CubeCorner.SquarePosition2 = 18
        CubeCorner.SquarePosition3 = 25
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 48
        CubeCorner.SquarePosition2 = 27
        CubeCorner.SquarePosition3 = 34
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 52
        CubeCorner.SquarePosition2 = 45
        CubeCorner.SquarePosition3 = 16
        self.__Corners.append(CubeCorner)

        CubeCorner = Corner()
        CubeCorner.SquarePosition1 = 54
        CubeCorner.SquarePosition2 = 36
        CubeCorner.SquarePosition3 = 43
        self.__Corners.append(CubeCorner)

    #
    # DefineCubeEdges
    # Define the edges of the cube for all faces
    def __DefineCubeEdges(self):
        # U
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 2
        CubeEdge.SquarePosition2 = 38
        self.__Edges.append(CubeEdge)
        
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 4
        CubeEdge.SquarePosition2 = 11
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 6
        CubeEdge.SquarePosition2 = 29
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 8
        CubeEdge.SquarePosition2 = 20
        self.__Edges.append(CubeEdge)

        # F
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 15
        CubeEdge.SquarePosition2 = 22
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 24
        CubeEdge.SquarePosition2 = 31
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 26
        CubeEdge.SquarePosition2 = 47
        self.__Edges.append(CubeEdge)

        # L
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 13
        CubeEdge.SquarePosition2 = 42
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 17
        CubeEdge.SquarePosition2 = 49
        self.__Edges.append(CubeEdge)

        # R
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 35
        CubeEdge.SquarePosition2 = 51
        self.__Edges.append(CubeEdge)

        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 33
        CubeEdge.SquarePosition2 = 40
        self.__Edges.append(CubeEdge)

        # B
        CubeEdge = Edge()
        CubeEdge.SquarePosition1 = 44
        CubeEdge.SquarePosition2 = 53
        self.__Edges.append(CubeEdge)

    #
    # FindCubeFaceSquareFromSquarePosition
    # Return the cube face using the square global position
    def __FindCubeFaceSquareFromSquarePosition(self, SquarePosition):
        CubeFace = self.__FindCubeFaceFromSquarePosition(SquarePosition = SquarePosition)
        if isinstance(CubeFace, Face):
            return CubeFace.GetSquareFromPosition(Position = SquarePosition)
        return None

    #
    # FindCubeFaceFromSquarePosition
    # Return the cube face using the square global position
    def __FindCubeFaceFromSquarePosition(self, SquarePosition):
        for CubeFace in self.__Faces.values():
            if SquarePosition >= CubeFace.LesserSquarePosition and SquarePosition <= CubeFace.GreaterSquarePosition:
                return CubeFace
        return None