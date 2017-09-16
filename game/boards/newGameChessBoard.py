from game.boards.chessBoard import ChessBoard
from game.pieces.bishop import Bishop
from game.pieces.king import King
from game.pieces.knight import Knight
from game.pieces.pawn import Pawn
from game.pieces.piece import Piece
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
			newGameMatrixOfPieces[0][column] = Piece()
			newGameMatrixOfPieces[1][column] = Pawn()
			newGameMatrixOfPieces[6][column] = Pawn()
			newGameMatrixOfPieces[7][column] = Piece()

		newGameMatrixOfPieces[0][2] = Bishop()
		newGameMatrixOfPieces[0][5] = Bishop()
		newGameMatrixOfPieces[7][2] = Bishop()
		newGameMatrixOfPieces[7][5] = Bishop()

		newGameMatrixOfPieces[0][3] = Queen()
		newGameMatrixOfPieces[7][3] = Queen()

		newGameMatrixOfPieces[0][4] = King()
		newGameMatrixOfPieces[7][4] = King()

		newGameMatrixOfPieces[0][1] = Knight()
		newGameMatrixOfPieces[0][6] = Knight()
		newGameMatrixOfPieces[7][1] = Knight()
		newGameMatrixOfPieces[7][6] = Knight()

		newGameMatrixOfPieces[0][0] = Rook()
		newGameMatrixOfPieces[0][7] = Rook()
		newGameMatrixOfPieces[7][0] = Rook()
		newGameMatrixOfPieces[7][7] = Rook()

		return newGameMatrixOfPieces
