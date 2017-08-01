from game.chessBoard import ChessBoard
from game.pieces.piece import Piece


class ChessGame(object):
	def __init__(self):
		super(ChessGame, self).__init__()
		self._board = ChessBoard(self._startingChessBoardDictionaryOfPiecesAndPositions())

	def board(self):
		return self._board

	def _startingChessBoardDictionaryOfPiecesAndPositions(self):
		aDictionaryOfPiecesAndPositions = dict()

		for column in range(8):
			aDictionaryOfPiecesAndPositions[(0, column)] = Piece()
			aDictionaryOfPiecesAndPositions[(1, column)] = Piece()
			aDictionaryOfPiecesAndPositions[(6, column)] = Piece()
			aDictionaryOfPiecesAndPositions[(7, column)] = Piece()

		return aDictionaryOfPiecesAndPositions