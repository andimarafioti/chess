from game.boards.chessBoard import ChessBoard
from game.pieces.piece import Piece


class NewGameChessBoard(ChessBoard):
	def __init__(self):
		aMatrixOfPieces = self._newGameMatrixOfPieces()
		super(NewGameChessBoard, self).__init__(aMatrixOfPieces)

	def _newGameMatrixOfPieces(self):
		newGameMatrixOfPieces = []
		for row in range(self.ROW_COUNT):
			newGameMatrixOfPieces.append([])
			for column in range(self.COLUMN_COUNT):
				newGameMatrixOfPieces[row].append(None)

		for column in range(self.COLUMN_COUNT):
			newGameMatrixOfPieces[0][column] = Piece()
			newGameMatrixOfPieces[1][column] = Piece()
			newGameMatrixOfPieces[6][column] = Piece()
			newGameMatrixOfPieces[7][column] = Piece()

		return newGameMatrixOfPieces
