from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay


class Player(object):
	def __init__(self, pieces):
		self._pieces = pieces

	def pieces(self):
		return self._pieces

	def nextPlay(self, aChessBoard):
		userInput = input('Insert next movement in Algebraic Notation --> ')
		aPlayInAlgebraicNotation = AlgebraicallyNotatedPlay(userInput, aChessBoard)
		return aPlayInAlgebraicNotation
