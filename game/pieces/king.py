from game.pieces.piece import Piece


class King(Piece):
	def canApplyAMovement(self, aMovement):
		return len(aMovement.path()) == 2
