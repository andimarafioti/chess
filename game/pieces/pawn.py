from game.pieces.piece import Piece


class Pawn(Piece):
	def canMoveFromTo(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		return True
