from unittest import TestCase

from game.chessBoard import ChessBoard
from game.chessGame import ChessGame
from game.pieces.piece import Piece


class TestChessGame(TestCase):
	def test01AGameHasABoard(self):
		aChessGame = ChessGame()

		self.assertIsInstance(aChessGame.board(), ChessBoard)

	def test02AGameHasABoardWithPieces(self):
		aChessGame = ChessGame()

		self.assertIsInstance(aChessGame.board().pieces(), list)

		for piece in aChessGame.board().pieces():
			self.assertIsInstance(piece, Piece)

	def test03AGameStartsWithABoardThatHas32Pieces(self):
		aChessGame = ChessGame()

		self.assertTrue(len(aChessGame.board().pieces()) is 32)
