class ChessBoard(object):
	ROW_COUNT = 8
	COLUMN_COUNT = 8

	def __init__(self, dictionaryOfPositionsAndPieces):
		super(ChessBoard, self).__init__()
		self._matrixOfPieces = []
		for row in range(self.ROW_COUNT):
			self._matrixOfPieces.append([])
			for column in range(self.COLUMN_COUNT):
				self._matrixOfPieces[row].append(None)

		self._initializeMatrixOfPiecesWith(dictionaryOfPositionsAndPieces)

	def pieces(self):
		pieces = []
		for row in range(self.ROW_COUNT):
			for column in range(self.COLUMN_COUNT):
				if self._matrixOfPieces[row][column]:
					pieces.append(self._matrixOfPieces[row][column])
		return pieces

	def _initializeMatrixOfPiecesWith(self, aDictionaryOfPositionsAndPieces):
		for row in range(self.ROW_COUNT):
			for column in range(self.COLUMN_COUNT):
				if aDictionaryOfPositionsAndPieces.has_key((row, column)):
					self._matrixOfPieces[row][column] = aDictionaryOfPositionsAndPieces[(row, column)]
