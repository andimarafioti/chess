from game.boards.chessBoard import ChessBoard
from game.pieces.piece import Piece
from game.pieces.rook import Rook


class King(Piece):
	def canApplyAMovement(self, aMovement):
		return len(aMovement.path()) == 2

	def isThisPlaySpecialForThisBoard(self, aPlay, aChessBoard):
		if not self.HAS_MOVED and self._isCastlingMovement(aPlay.movement()):
			aRook = None
			if self._isCastlingToTheLeft(aPlay.movement()):
				aRook = aChessBoard.pieceAt(aPlay.movement().initialRow(), 0)
			elif self._isCastlingToTheRight(aPlay.movement()):
				aRook = aChessBoard.pieceAt(aPlay.movement().initialRow(), 7)
			return isinstance(aRook, Rook) and not aRook.HAS_MOVED
		return super(King, self).isThisPlaySpecialForThisBoard(aPlay, aChessBoard)

	def _isCastlingMovement(self, aMovement):
		return aMovement.initialRow() == aMovement.newRow() and \
			   abs(aMovement.initialColumn() - aMovement.newColumn()) == 2

	def _isCastlingToTheLeft(self, aMovement):
		return aMovement.initialColumn() - aMovement.newColumn() == 2

	def _isCastlingToTheRight(self, aMovement):
		return aMovement.newColumn() - aMovement.initialColumn() == 2

	def applySpecialConsequencesOfAPlayToABoard(self, aPlay, aChessBoard):
		if self._isCastlingToTheLeft(aPlay.movement()):
			matrixOfPieces = aChessBoard.matrixOfPieces()
			aRook = aChessBoard.pieceAt(aPlay.movement().initialRow(), 0)
			matrixOfPieces[aPlay.movement().initialRow()][0] = None
			matrixOfPieces[aPlay.movement().initialRow()][3] = aRook
			newChessBoard = ChessBoard(matrixOfPieces)
			aRook.hasMoved()
			return newChessBoard
		elif self._isCastlingToTheRight(aPlay.movement()):
			matrixOfPieces = aChessBoard.matrixOfPieces()
			aRook = aChessBoard.pieceAt(aPlay.movement().initialRow(), 7)
			matrixOfPieces[aPlay.movement().initialRow()][7] = None
			matrixOfPieces[aPlay.movement().initialRow()][5] = aRook
			newChessBoard = ChessBoard(matrixOfPieces)
			aRook.hasMoved()
			return newChessBoard
