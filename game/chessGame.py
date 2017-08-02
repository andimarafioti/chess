from game.boards.newGameChessBoard import NewGameChessBoard
from game.pieces.invalidMovementError import InvalidMovementError


class ChessGame(object):
	def __init__(self):
		super(ChessGame, self).__init__()
		self._board = NewGameChessBoard()

	def board(self):
		return self._board

	def pieceAt(self, aRow, aColumn):
		return self._board.pieceAt(aRow, aColumn)

	def moveAPieceFromAPositionToAnother(self, aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		self._board = self._board.moveAPieceFromAPositionToAnother(aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn)

	def applyAPlay(self, aPlay):
		try:
			newBoard = self._board.applyAPlay(aPlay)
		except InvalidMovementError, e:
			raise e
		self._board = newBoard