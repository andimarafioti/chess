from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.pieces.bishop import Bishop
from game.pieces.knight import Knight
from game.pieces.queen import Queen
from game.pieces.rook import Rook
from game.player import Player


class ConsolePlayer(Player):
    def chooseNewRankForPawn(self, aPawn):
        userInput = int(input('Promote Pawn to (Insert 1 For Queen, 2 for Knight, 3 for Rook or 4 for Bishop: '))
        if userInput is 1:
            return Queen(aPawn.isWhite())
        elif userInput is 2:
            return Knight(aPawn.isWhite())
        elif userInput is 3:
            return Rook(aPawn.isWhite())
        elif userInput is 4:
            return Bishop(aPawn.isWhite())
        else:
            raise Exception("One would think instructions were clear...")

    def _getPlayFromUser(self, aChessBoard):
        userInput = input('Insert next movement in Algebraic Notation --> ')
        aPlay = AlgebraicallyNotatedPlay(userInput, aChessBoard)
        return aPlay
