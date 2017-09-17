from game.movements.invalidMovementError import InvalidMovementError


class ChessBoard(object):
	ROW_COUNT = 8
	COLUMN_COUNT = 8

	def __init__(self, aMatrixOfPieces):
		super(ChessBoard, self).__init__()
		assert len(aMatrixOfPieces) is 8, "Tried to initialize a Board with a wrong size"
		assert len(aMatrixOfPieces[0]) is 8, "Tried to initialize a Board with a wrong size"

		self._matrixOfPieces = aMatrixOfPieces

	def __repr__(self):
		output = ""
		matrix = self._matrixOfPieces[:]
		matrix.reverse()
		for column in matrix:
			output += str(column) + "\n"
		return output

	def pieces(self):
		pieces = []
		for row in range(self.ROW_COUNT):
			for column in range(self.COLUMN_COUNT):
				if self._matrixOfPieces[row][column]:
					pieces.append(self._matrixOfPieces[row][column])
		return pieces

	def pieceAt(self, aRow, aColumn):
		return self._matrixOfPieces[aRow][aColumn]

	def applyAPlay(self, aPlay):
		if not aPlay.piece() == self._matrixOfPieces[aPlay.initialRow()][aPlay.initialColumn()]:
			raise InvalidMovementError
		if not aPlay.piece().canApplyAMovement(aPlay.movement()):
			raise InvalidMovementError("The piece doesn't move like that")
		if not self.canApplyAPlaysPath(aPlay):
			raise InvalidMovementError("The path is blocked!")

		self._matrixOfPieces[aPlay.initialRow()][aPlay.initialColumn()] = None
		self._matrixOfPieces[aPlay.newRow()][aPlay.newColumn()] = aPlay.piece()

		return ChessBoard(self._matrixOfPieces)

	def canApplyAPlaysPath(self, aPlay):
		return aPlay.piece().canJumpAnotherPiece() or self._movementsPathIsUnocupied(aPlay.movement())

	def _movementsPathIsUnocupied(self, aMovement):
		path = aMovement.path()
		intermediary_path = path[1:len(path) - 1]
		is_ocuppied = []
		for row, column in intermediary_path:
			is_ocuppied.append(self._matrixOfPieces[row][column] is None)
		return all(is_ocuppied)
