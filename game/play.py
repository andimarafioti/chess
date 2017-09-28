from game.boards.chessBoard import ChessBoard
from game.pieces.piece import Piece


class Play(object):
	def __init__(self, aPiece, aMovement):
		assert isinstance(aPiece, Piece), 'A play has to involve a Piece'
		self._aPiece = aPiece
		self._aMovement = aMovement
		self._hasConsequencesAfterApplied = False

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

	def pieceCanApplyAMovement(self):
		return self._aPiece.canApplyAMovement(self._aMovement) #  or self._aPiece.canApplyASpecialPlay(self)

	# def hasConsequencesAfterApplied(self):
	# 	return self._hasConsequencesAfterApplied
    #
	# def applyConsequenquencesToBoard(self, chessBoard):
    #
	# 	newChessBoard = ChessBoard()
    #
	# def setSpecialPlayConsequence(self, ):

