from game.boards.chessBoard import ChessBoard
from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn
from game.pieces.queen import Queen
from game.pieces.rook import Rook


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
			newGameMatrixOfPieces[1][column] = Pawn(isWhite=True)
			newGameMatrixOfPieces[6][column] = Pawn(isWhite=False)

		newGameMatrixOfPieces[0][2] = Bishop(isWhite=True)
		newGameMatrixOfPieces[0][5] = Bishop(isWhite=True)
		newGameMatrixOfPieces[7][2] = Bishop(isWhite=False)
		newGameMatrixOfPieces[7][5] = Bishop(isWhite=False)

		newGameMatrixOfPieces[0][3] = Queen(isWhite=True)
		newGameMatrixOfPieces[7][3] = Queen(isWhite=False)

		newGameMatrixOfPieces[0][4] = King(isWhite=True)
		newGameMatrixOfPieces[7][4] = King(isWhite=False)

		newGameMatrixOfPieces[0][1] = Knight(isWhite=True)
		newGameMatrixOfPieces[0][6] = Knight(isWhite=True)
		newGameMatrixOfPieces[7][1] = Knight(isWhite=False)
		newGameMatrixOfPieces[7][6] = Knight(isWhite=False)

		newGameMatrixOfPieces[0][0] = Rook(isWhite=True)
		newGameMatrixOfPieces[0][7] = Rook(isWhite=True)
		newGameMatrixOfPieces[7][0] = Rook(isWhite=False)
		newGameMatrixOfPieces[7][7] = Rook(isWhite=False)

		return newGameMatrixOfPieces
