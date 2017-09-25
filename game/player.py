from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay


class Player(object):
	def __init__(self, pieces):
		self._pieces = pieces

	def pieces(self):
		return self._pieces

	def nextPlay(self, aChessBoard):
		aPlay = self._getPlayFromUser(aChessBoard)
		return aPlay

	def _getPlayFromUser(self, aChessBoard):
		userInput = input('Insert next movement in Algebraic Notation --> ')
		aPlay = AlgebraicallyNotatedPlay(userInput, aChessBoard)
		self._assertPlayIsValid(aPlay)
		return aPlay

	def _assertPlayIsValid(self, aPlay):
		assert aPlay.piece() in self._pieces, "a Player can't move a piece that doesn't belong to him"
