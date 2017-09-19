from unittest import TestCase

from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.boards.chessBoard import ChessBoard
from game.chessGame import ChessGame
from game.movements.invalidMovementError import InvalidMovementError
from game.movements.movement import Movement
from game.pieces.pawn import Pawn
from game.pieces.piece import Piece
from game.play import Play
from game.player import Player


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

    def test11aQueenCanMoveInDiagonals(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=2)
        aMovement = Movement(anInitialRow=1, anInitialColumn=2, aNewRow=3, aNewColumn=2)
        aQueenFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessGame.applyAPlay(aQueenFreeingPlay)

        aQueen = aChessGame.pieceAt(aRow=0, aColumn=3)
        aMovement = Movement(anInitialRow=0, anInitialColumn=3, aNewRow=2, aNewColumn=1)
        aPlay = Play(aPiece=aQueen, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        self.assertEqual(aChessGame.pieceAt(aRow=2, aColumn=1), aQueen)

    def test12aQueenCanMoveStraight(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=3)
        aMovement = Movement(anInitialRow=1, anInitialColumn=3, aNewRow=3, aNewColumn=3)
        aQueenFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessGame.applyAPlay(aQueenFreeingPlay)

        aQueen = aChessGame.pieceAt(aRow=0, aColumn=3)
        aMovement = Movement(anInitialRow=0, anInitialColumn=3, aNewRow=2, aNewColumn=3)
        aPlay = Play(aPiece=aQueen, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        self.assertEqual(aChessGame.pieceAt(aRow=2, aColumn=3), aQueen)

    def test13aKnightCanJump(self):
        aChessGame = ChessGame()

        aKnight = aChessGame.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=2)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        self.assertEqual(aChessGame.pieceAt(aRow=2, aColumn=2), aKnight)

    def test14aKnightCantMoveInDiagonals(self):
        aChessGame = ChessGame()

        aKnight = aChessGame.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=3)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)

    def test15aKnightCantMoveStraight(self):
        aChessGame = ChessGame()

        aKnight = aChessGame.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=1)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)

    def test16aKnightCantMove2StepsForwardAnd3StepsToASide(self):
        aChessGame = ChessGame()

        aKnight = aChessGame.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=4)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)

    def test17aRookCanMoveInAStraightLine(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aRookFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessGame.applyAPlay(aRookFreeingPlay)

        aRook = aChessGame.pieceAt(aRow=0, aColumn=0)
        aMovement = Movement(anInitialRow=0, anInitialColumn=0, aNewRow=2, aNewColumn=0)
        aPlay = Play(aPiece=aRook, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        self.assertEqual(aChessGame.pieceAt(aRow=2, aColumn=0), aRook)

    def test18aKingCanMoveInAnyDirectionOneStepAtATime(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=4)
        aMovement = Movement(anInitialRow=1, anInitialColumn=4, aNewRow=3, aNewColumn=4)
        aKingFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessGame.applyAPlay(aKingFreeingPlay)

        aKing = aChessGame.pieceAt(aRow=0, aColumn=4)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=1, aNewColumn=4)
        aPlay = Play(aPiece=aKing, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        self.assertEqual(aChessGame.pieceAt(aRow=1, aColumn=4), aKing)

    def test20aPlayInAlgebraicNotationCanBeApplied(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=4)
        aPlayInAlgebraicNotation = AlgebraicallyNotatedPlay('e2 e4', aChessGame)
        aChessGame.applyAPlay(aPlayInAlgebraicNotation)

        self.assertEqual(aChessGame.pieceAt(aRow=3, aColumn=4), aPawn)

    def test21aGameHasTwoPlayers(self):
        aChessGame = ChessGame()
        players = aChessGame.players()

        self.assertTrue(len(players) == 2)
        self.assertIsInstance(players[0], Player)
        self.assertIsInstance(players[1], Player)

    def test22aPlayHasToInvolveAPiece(self):
        aChessGame = ChessGame()

        nothing = aChessGame.pieceAt(aRow=3, aColumn=4)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=1, aNewColumn=4)
        with self.assertRaises(AssertionError):
            aPlay = Play(aPiece=nothing, aMovement=aMovement)

    def test23aPlayerKnowsItsPieces(self):
        aChessGame = ChessGame()
        aPlayer = aChessGame.players()[0]

        aPlayersPieces = aPlayer.pieces()

        self.assertTrue(len(aPlayersPieces) == 16)
        for piece in aPlayersPieces:
            self.assertIsInstance(piece, Piece)

        boardPieces = aChessGame.board().pieces()
        self.assertTrue(all([piece in boardPieces for piece in aPlayersPieces]))

    def test24aPawnCantMoveBackwards(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        aPawn = aChessGame.pieceAt(aRow=3, aColumn=0)
        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=2, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)

    def test25aPawnSecondMovementCanBeTwoSpacesForward(self):
        aChessGame = ChessGame()

        aPawn = aChessGame.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        aChessGame.applyAPlay(aPlay)

        aPawn = aChessGame.pieceAt(aRow=3, aColumn=0)
        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=5, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)

    def test26aPawnCanMoveInADiagonalIfItsCapturingAnEnemysPiece(self):
        aChessGame = ChessGame()

        aWhitePawn = aChessGame.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aWhitePawn, aMovement=aMovement)
        aChessGame.applyAPlay(aPlay)

        aBlackPawn = aChessGame.pieceAt(aRow=6, aColumn=1)
        aMovement = Movement(anInitialRow=6, anInitialColumn=1, aNewRow=4, aNewColumn=1)
        aPlay = Play(aPiece=aBlackPawn, aMovement=aMovement)
        aChessGame.applyAPlay(aPlay)

        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=4, aNewColumn=1)
        aPlay = Play(aPiece=aWhitePawn, aMovement=aMovement)
        aChessGame.applyAPlay(aPlay)

        self.assertTrue(aChessGame.pieceAt(4, 1) is aWhitePawn)

    def test27aPieceCannotCaptureApieceFromItsSameTeam(self):
        aChessGame = ChessGame()

        aRook = aChessGame.pieceAt(aRow=0, aColumn=0)
        aMovement = Movement(anInitialRow=0, anInitialColumn=0, aNewRow=1, aNewColumn=0)
        aPlay = Play(aPiece=aRook, aMovement=aMovement)
        with self.assertRaises(InvalidMovementError):
            aChessGame.applyAPlay(aPlay)
