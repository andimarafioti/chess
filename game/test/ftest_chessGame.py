from unittest import TestCase

from game.boards.chessBoard import ChessBoard
from game.chessGame import ChessGame
from game.pieces.pawn import Pawn
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

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)

		aChessGame.moveAPieceFromAPositionToAnother(aPiece=aPawn, anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)

		self.assertEqual(aChessGame.pieceAt(aRow=3, aColumn=0), aPawn)

	def test05TheGameDoesntAcceptAMovementIfThePieceIsNotAtTheInitialPosition(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)

		with self.assertRaises(AssertionError):
			aChessGame.moveAPieceFromAPositionToAnother(aPiece=aPawn, anInitialRow=1, anInitialColumn=1, aNewRow=3, aNewColumn=0)

	def test06UponInitializationAnyPieceAtTheSecondRowIsAPawn(self):
		aChessGame = ChessGame()
		aListOfPawns = [aChessGame.pieceAt(aRow=1, aColumn=column) for column in range(8)]

		for pawn in aListOfPawns:
			self.assertIsInstance(pawn, Pawn)
