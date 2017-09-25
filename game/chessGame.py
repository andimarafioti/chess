from utils.subject import Subject
from utils.worker.worker import Worker


class ChessGame(object):
	BOARD_CHANGE = "theBoardChanged"

	def __init__(self, board, firstPlayPlayer, secondPlayPlayer):
		super(ChessGame, self).__init__()
		self._board = board
		self._players = [firstPlayPlayer, secondPlayPlayer]
		self._nextTurnPlayer = firstPlayPlayer
		self._subject = Subject(self)
		Worker.call(self.gameRoutine).asDaemon.start()

	def subject(self):
		return self._subject

	def board(self):
		return self._board

	def pieceAt(self, aRow, aColumn):
		return self._board.pieceAt(aRow, aColumn)

	def moveAPieceFromAPositionToAnother(self, aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		self._board = self._board.moveAPieceFromAPositionToAnother(aPiece, anInitialRow, anInitialColumn, aNewRow, aNewColumn)

	def players(self):
		return self._players

	def gameRoutine(self):
		while True:
			try:
				aPlay = self._nextTurnPlayer.nextPlay(self._board)
				newBoard = self._board.applyAPlay(aPlay)
				self._nextTurnPlayer = [player for player in self._players if player is not self._nextTurnPlayer][0]
				self._board = newBoard
				self._subject.notify(self.BOARD_CHANGE)
			except Exception as e:
				print(e)
