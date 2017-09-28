from game.boards.chessBoard import ChessBoard
from game.pieces.piece import Piece


class Play(object):
	def __init__(self, aPiece, aMovement):
		assert isinstance(aPiece, Piece), 'A play has to involve a Piece'
		self._aPiece = aPiece
		self._aMovement = aMovement

	def piece(self):
		return self._aPiece

	def movement(self):
		return self._aMovement

	def initialRow(self):
		return self._aMovement.initialRow()

	def newRow(self):
		return self._aMovement.newRow()

	def initialColumn(self):
		return self._aMovement.initialColumn()

	def newColumn(self):
		return self._aMovement.newColumn()

	def pieceMovesLikeThis(self):
		return self._aPiece.canApplyAMovement(self._aMovement)

	def isSpecialForThisBoard(self, aChessBoard):
		return self._aPiece.isThisPlaySpecialForThisBoard(self, aChessBoard)

	def applySpecialConsequencesToThisBoard(self, aChessBoard):
		return self._aPiece.applySpecialConsequencesOfAPlayToABoard(self, aChessBoard)
