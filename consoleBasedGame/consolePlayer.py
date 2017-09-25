from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.player import Player


class ConsolePlayer(Player):
    def _getPlayFromUser(self, aChessBoard):
        userInput = input('Insert next movement in Algebraic Notation --> ')
        aPlay = AlgebraicallyNotatedPlay(userInput, aChessBoard)
        return aPlay
