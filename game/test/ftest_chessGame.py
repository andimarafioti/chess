from unittest import TestCase

from game.chessBoard import ChessBoard
from game.chessGame import ChessGame


class TestChessGame(TestCase):
	def test01AGameHasABoard(self):
		aChessGame = ChessGame()

		self.assertIsInstance(aChessGame.board(), ChessBoard)