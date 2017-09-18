from game.boards.newGameChessBoard import NewGameChessBoard
from game.movements.invalidMovementError import InvalidMovementError
from game.player import Player


class ChessGame(object):
	def __init__(self):
		super(ChessGame, self).__init__()
		self._board = NewGameChessBoard()
		self._players = [Player(self._board.whitePieces()), Player(self._board.blackPieces())]

	def isFinished(self):
		return False

	def board(self):
		return self._board

	def pieceAt(self, aRow, aColumn):
		return self._board.pieceAt(aRow, aColumn)

	def moveAPieceFromAPositionToAnother(self, aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		self._board = self._board.moveAPieceFromAPositionToAnother(aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn)

	def applyAPlay(self, aPlay):
		try:
			newBoard = self._board.applyAPlay(aPlay)
		except InvalidMovementError as e:
			raise e
		self._board = newBoard

	def players(self):
		return self._players
