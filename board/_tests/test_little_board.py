import unittest
from board.little_board import LittleBoard


board = LittleBoard()
board.PrintBoard()
print("")
board.MakePlay(1, 1, 2)
board.PrintBoard()
print("")
board.MakePlay(2, 2, 2)
board.PrintBoard()
print("")
board.MakePlay(1, 1, 2)

class Test(unittest.TestCase):


    def testLittleBoardVictories(self):
        pass
        #self.assertEqual(board.GetStatus(), board.STATUS_PLAYER_ONE_WON)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()