from unittest import TestCase

from game.boards.chessBoard import ChessBoard
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

	def test04TheGameAcceptsAMovement(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=2, aColumn=0)

		aChessGame.moveAPieceToAPosition(aPiece=aPawn, aNewRow=4, aNewColumn=0)

		self.assertEqual(aChessGame.pieceAt(row=4, column=0), aPawn)
