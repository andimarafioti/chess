from game.pieces.piece import Piece


class Pawn(Piece):
	COUNT_OF_SPACES_I_CAN_MOVE_FORWARD = 2

	def canApplyAMovement(self, aMovement):
		return aMovement.initialColumn() == aMovement.newColumn() and \
			self._movementIsOneOrTwoStepsInTheRightDirection(aMovement)

	def _movementIsOneOrTwoStepsInTheRightDirection(self, aMovement):
		if self._isWhite:
			condition = 0 < aMovement.newRow() - aMovement.initialRow() <= self.COUNT_OF_SPACES_I_CAN_MOVE_FORWARD
		else:
			condition = 0 < aMovement.initialRow() - aMovement.newRow() <= self.COUNT_OF_SPACES_I_CAN_MOVE_FORWARD
		return condition

	def appliedPlay(self, aPlay):
		self.COUNT_OF_SPACES_I_CAN_MOVE_FORWARD = 1
