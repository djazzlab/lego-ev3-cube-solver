class Edge:
    _SquarePosition1 = 0
    _SquarePosition2 = 0

    def __init__(self):
        return

    ######################
    # Properties Methods #
    ######################
    #
    # SquarePosition1 property
    @property
    def SquarePosition1(self):
        return self._SquarePosition1

    @SquarePosition1.setter
    def SquarePosition1(self, SquarePosition):
        if not isinstance(SquarePosition, int):
            raise ValueError('Not integer SquarePosition1 is not possible')

        self._SquarePosition1 = SquarePosition

    @SquarePosition1.deleter
    def SquarePosition1(self):
        del self._SquarePosition1

    #
    # SquarePosition2 property
    @property
    def SquarePosition2(self):
        return self._SquarePosition2

    @SquarePosition2.setter
    def SquarePosition2(self, SquarePosition):
        if not isinstance(SquarePosition, int):
            raise ValueError('Not integer SquarePosition2 is not possible')

        self._SquarePosition2 = SquarePosition

    @SquarePosition2.deleter
    def SquarePosition2(self):
        del self._SquarePosition2