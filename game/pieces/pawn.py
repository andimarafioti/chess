from game.pieces.piece import Piece


class Pawn(Piece):
	def canApplyAMovement(self, aMovement):
		return aMovement.initialColumn() == aMovement.newColumn() and \
			self._movementIsOneOrTwoStepsInTheRightDirection(aMovement)

	def _movementIsOneOrTwoStepsInTheRightDirection(self, aMovement):
		if self.HAS_MOVED:
			return self._movementIsXStepsInTheRightDirection(aMovement, 1)
		else:
			return self._movementIsXStepsInTheRightDirection(aMovement, 2)

	def _movementIsXStepsInTheRightDirection(self, aMovement, x):
		if self._isWhite:
			condition = 0 < aMovement.newRow() - aMovement.initialRow() <= x
		else:
			condition = 0 < aMovement.initialRow() - aMovement.newRow() <= x
		return condition

	def canCaptureAnotherPieceWithAMovement(self, aMovement):
		return 0 < abs(aMovement.initialColumn() - aMovement.newColumn()) < 2 and \
			self._movementIsXStepsInTheRightDirection(aMovement, 1)

	def isThisPlaySpecialForThisBoard(self, aPlay, aChessBoard):
		return self._playPromotesMe(aPlay)

	def applySpecialConsequencesOfAPlayToABoard(self, aPlay, aBoard):
		if self._playPromotesMe(aPlay):
			raise PromotePawnException()
		raise Exception("Pawn doesnt know this weird play")

	def _playPromotesMe(self, aPlay):
		return self._isWhite and aPlay.newRow() is 7 or not self._isWhite and aPlay.newRow() is 0


class PromotePawnException(Exception):
	pass
