from game.boards.newGameChessBoard import NewGameChessBoard


class ChessGame(object):
	def __init__(self):
		super(ChessGame, self).__init__()
		self._board = NewGameChessBoard()

	def board(self):
		return self._board

	def pieceAt(self, aRow, aColumn):
		return self._board.pieceAt(aRow, aColumn)

	def moveAPieceToAPosition(self, aPiece, aNewRow, aNewColumn):
		pass
