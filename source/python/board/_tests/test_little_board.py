import unittest
from source.python.board.little_board import LittleBoard


class Test(unittest.TestCase):


    def testLittleBoardVictories(self):
        board = LittleBoard()
        for i in range(3):
            print(board._board[i][0],board._board[i][1],board._board[i][2])
        board._board[0][0] = 1
        board._board[1][0] = 1
        board._board[2][0] = 1
        self.assertEqual(board.GetStatus(), board.STATUS_PLAYER_ONE_WON)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()