


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
        for p in [1,2]:
            # first check for a row-win for player p
            for r in range(3):
                if self._board[r][0] == self._board[r][1] == self._board[r][2] == p:
                    return p
            # then check for a column-win for player p
            for c in range(3):
                if self._board[0][c] == self._board[1][c] == self._board[1][c] == p:
                    return p
            # finally, check for a diagonal-win for player p
            if self._board[0][0] == self._board[1][1] == self._board[2][2] == p or self._board[2][0] == self._board[1][1] == self._board[0][2] == p:
                return p

        # if none of the above, check for open slots
        for r in range(3):
            for c in range(3):
                if self._board[r][c] == 0:
                    return 0

        # none of the above, so it's a tie
        return 3

    def MakePlay(self, player, row, column):
        if self._board[row][column] == 0:
            self._board[row][column] = player
        else:
            print("Move not allowed")

    def PrintBoard(self):
        for r in range(3):
            print(self._board[r][0],self._board[r][1],self._board[r][2])