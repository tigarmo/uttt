


class LittleBoard(object):
    STATUS_PLAYABLE = 0
    STATUS_PLAYER_ONE_WON = 1
    STATUS_PLAYER_TWO_WON = 2
    STATUS_TIE = 3

    def __init__(self):
        def CreateEmptyRow():
            return [0 for _ in range(3)]
        self._board = [ CreateEmptyRow() for _ in range(3)]

    def GetStatus(self):
        pass