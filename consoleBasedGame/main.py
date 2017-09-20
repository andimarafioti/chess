from time import sleep

from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.boards.newGameChessBoard import NewGameChessBoard
from game.chessGame import ChessGame
from game.player import Player

aBoard = NewGameChessBoard()
twoPlayers = [Player(aBoard.whitePieces()), Player(aBoard.blackPieces())]
aChessGame = ChessGame(aBoard, twoPlayers[0], twoPlayers[1])


class ChessGameObserver(object):
    def __init__(self, aChessGame):
        aChessGame.subject().addObserver(self)

    def onNotify(self, emitter, event, args):
        print(emitter.board())

aChessGameObserver = ChessGameObserver(aChessGame)

sleep(100)
