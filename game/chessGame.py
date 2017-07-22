from game.chessBoard import ChessBoard


class ChessGame(object):
	def __init__(self):
		super(ChessGame, self).__init__()
		self._board = ChessBoard()

	def board(self):
		return self._board