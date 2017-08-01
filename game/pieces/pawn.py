from game.pieces.piece import Piece


class Pawn(Piece):
	def canMoveFromTo(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		return self._movementIsOneOrTwoStepsInAnyDirection(anInitialRow, anInitialColumn, aNewRow, aNewColumn)

	def _movementIsOneOrTwoStepsInAnyDirection(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		return anInitialColumn == aNewColumn and 0 < abs(anInitialRow - aNewRow) < 3
