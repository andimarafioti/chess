from unittest import TestCase

from game.boards.chessBoard import ChessBoard
from game.chessGame import ChessGame
from game.pieces.invalidMovementError import InvalidMovementError
from game.pieces.movement import Movement
from game.pieces.pawn import Pawn
from game.pieces.piece import Piece
from game.play import Play


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

	def test04TheGameAcceptsAPlay(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
		aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
		aPlay = Play(aPiece=aPawn, aMovement=aMovement)

		aChessGame.applyAPlay(aPlay)

		self.assertEqual(aChessGame.pieceAt(aRow=3, aColumn=0), aPawn)

	def test05TheGameDoesntAcceptAPlayIfThePieceIsNotAtTheInitialPosition(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
		aMovement = Movement(anInitialRow=1, anInitialColumn=1, aNewRow=3, aNewColumn=0)
		aPlay = Play(aPiece=aPawn, aMovement=aMovement)

		with self.assertRaises(InvalidMovementError):
			aChessGame.applyAPlay(aPlay)

	def test06UponInitializationAnyPieceAtTheSecondRowIsAPawn(self):
		aChessGame = ChessGame()
		aListOfPawns = [aChessGame.pieceAt(aRow=1, aColumn=column) for column in range(8)]

		for pawn in aListOfPawns:
			self.assertIsInstance(pawn, Pawn)

	def test07aPawnFirstMovementCantBeMovingForwardThreeSpaces(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
		aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=4, aNewColumn=0)
		aPlay = Play(aPiece=aPawn, aMovement=aMovement)

		with self.assertRaises(InvalidMovementError):
			aChessGame.applyAPlay(aPlay)

	def test08aBishopMovesInDiagonals(self):
		aChessGame = ChessGame()

		aPawn = aChessGame.pieceAt(aRow=1, aColumn=3)
		aMovement = Movement(anInitialRow=1, anInitialColumn=3, aNewRow=3, aNewColumn=3)
		aBishopFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
		aChessGame.applyAPlay(aBishopFreeingPlay)

		aBishop = aChessGame.pieceAt(aRow=0, aColumn=2)
		aMovement = Movement(anInitialRow=0, anInitialColumn=2, aNewRow=2, aNewColumn=4)
		aPlay = Play(aPiece=aBishop, aMovement=aMovement)

		aChessGame.applyAPlay(aPlay)

		self.assertEqual(aChessGame.pieceAt(aRow=2, aColumn=4), aBishop)

	def test09aMovementHasToChangeItsPosition(self):
		with self.assertRaises(InvalidMovementError):
			Movement(anInitialRow=0, anInitialColumn=2, aNewRow=0, aNewColumn=2)

	def test10aBishopCantApplyAMovementThatHasAnotherPieceInItsPath(self):
		aChessGame = ChessGame()

		aBishop = aChessGame.pieceAt(aRow=0, aColumn=2)
		aMovement = Movement(anInitialRow=0, anInitialColumn=2, aNewRow=2, aNewColumn=4)
		aPlay = Play(aPiece=aBishop, aMovement=aMovement)

		with self.assertRaises(InvalidMovementError):
			aChessGame.applyAPlay(aPlay)

