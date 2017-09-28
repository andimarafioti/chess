from time import sleep

from consoleBasedGame.consolePlayer import ConsolePlayer
from game.boards.newGameChessBoard import NewGameChessBoard
from game.chessGame import ChessGame

aBoard = NewGameChessBoard()
twoPlayers = [ConsolePlayer(aBoard.whitePieces()), ConsolePlayer(aBoard.blackPieces())]
aChessGame = ChessGame(aBoard, twoPlayers[0], twoPlayers[1])
print(aChessGame.board())


class ChessGameObserver(object):
    def __init__(self, aChessGame):
        aChessGame.subject().addObserver(self)

    def onNotify(self, emitter, event, args):
        print(emitter.board())

aChessGameObserver = ChessGameObserver(aChessGame)
aChessGame.startGameRoutine()

while True:
    sleep(100)
