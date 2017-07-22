class ChessBoard(object):
	ROW_COUNT = 8
	COLUMN_COUNT = 8

	def __init__(self, dictionaryOfPositionsAndPieces):
		super(ChessBoard, self).__init__()
		self._matrixOfPieces = [[]]
		self._initializeMatrixOfPiecesWith(dictionaryOfPositionsAndPieces)

	def pieces(self):
		return self._matrixOfPieces

	def _initializeMatrixOfPiecesWith(self, aDictionaryOfPositionsAndPieces):
		self._matrixOfPieces = [[None] * self.ROW_COUNT] * self.COLUMN_COUNT
		for row in range(self.ROW_COUNT):
			for column in range(self.COLUMN_COUNT):
				if aDictionaryOfPositionsAndPieces.has_key((row, column)):
					self._matrixOfPieces[row][column] = aDictionaryOfPositionsAndPieces[(row, column)]
