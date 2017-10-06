from unittest import TestCase

from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.boards.chessBoard import ChessBoard
from game.boards.newGameChessBoard import NewGameChessBoard
from game.chessGame import ChessGame
from game.movements.invalidMovementError import InvalidMovementError
from game.movements.movement import Movement
from game.pieces.pawn import Pawn
from game.pieces.piece import Piece
from game.pieces.queen import Queen
from game.play import Play
from game.player import Player


class TestChessGame(TestCase):
    def test01AGameHasaChessBoard(self):
        aChessBoard = NewGameChessBoard()
        twoPlayers = [Player(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]
        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])

        self.assertIsInstance(aChessGame.board(), ChessBoard)

    def test02AGameHasAChessBoardWithPieces(self):
        aChessBoard = NewGameChessBoard()
        twoPlayers = [Player(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]
        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])

        self.assertIsInstance(aChessGame.board().pieces(), list)

        for piece in aChessGame.board().pieces():
            self.assertIsInstance(piece, Piece)

    def test03AGameStartsWithaChessBoardThatHas32Pieces(self):
        aChessBoard = NewGameChessBoard()
        twoPlayers = [Player(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]
        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])

        self.assertTrue(len(aChessGame.board().pieces()) is 32)

    def test04TheBoardAcceptsAPlay(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=3, aColumn=0), aPawn)

    def test05TheBoardDoesntAcceptAPlayIfThePieceIsNotAtTheInitialPosition(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=1, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test06UponInitializationOfANewBoardAnyPieceAtTheSecondRowIsAPawn(self):
        aChessBoard = NewGameChessBoard()
        aListOfPawns = [aChessBoard.pieceAt(aRow=1, aColumn=column) for column in range(8)]

        for pawn in aListOfPawns:
            self.assertIsInstance(pawn, Pawn)

    def test07aPawnFirstMovementCantBeMovingForwardThreeSpaces(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=4, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test08aBishopMovesInDiagonals(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=3)
        aMovement = Movement(anInitialRow=1, anInitialColumn=3, aNewRow=3, aNewColumn=3)
        aBishopFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aBishopFreeingPlay)

        aBishop = aChessBoard.pieceAt(aRow=0, aColumn=2)
        aMovement = Movement(anInitialRow=0, anInitialColumn=2, aNewRow=2, aNewColumn=4)
        aPlay = Play(aPiece=aBishop, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=2, aColumn=4), aBishop)

    def test09aMovementHasToChangeItsPosition(self):
        with self.assertRaises(InvalidMovementError):
            Movement(anInitialRow=0, anInitialColumn=2, aNewRow=0, aNewColumn=2)

    def test10aBishopCantApplyAMovementThatHasAnotherPieceInItsPath(self):
        aChessBoard = NewGameChessBoard()

        aBishop = aChessBoard.pieceAt(aRow=0, aColumn=2)
        aMovement = Movement(anInitialRow=0, anInitialColumn=2, aNewRow=2, aNewColumn=4)
        aPlay = Play(aPiece=aBishop, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test11aQueenCanMoveInDiagonals(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=2)
        aMovement = Movement(anInitialRow=1, anInitialColumn=2, aNewRow=3, aNewColumn=2)
        aQueenFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aQueenFreeingPlay)

        aQueen = aChessBoard.pieceAt(aRow=0, aColumn=3)
        aMovement = Movement(anInitialRow=0, anInitialColumn=3, aNewRow=2, aNewColumn=1)
        aPlay = Play(aPiece=aQueen, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=2, aColumn=1), aQueen)

    def test12aQueenCanMoveStraight(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=3)
        aMovement = Movement(anInitialRow=1, anInitialColumn=3, aNewRow=3, aNewColumn=3)
        aQueenFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aQueenFreeingPlay)

        aQueen = aChessBoard.pieceAt(aRow=0, aColumn=3)
        aMovement = Movement(anInitialRow=0, anInitialColumn=3, aNewRow=2, aNewColumn=3)
        aPlay = Play(aPiece=aQueen, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=2, aColumn=3), aQueen)

    def test13aKnightCanJump(self):
        aChessBoard = NewGameChessBoard()

        aKnight = aChessBoard.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=2)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=2, aColumn=2), aKnight)

    def test14aKnightCantMoveInDiagonals(self):
        aChessBoard = NewGameChessBoard()

        aKnight = aChessBoard.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=3)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test15aKnightCantMoveStraight(self):
        aChessBoard = NewGameChessBoard()

        aKnight = aChessBoard.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=1)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test16aKnightCantMove2StepsForwardAnd3StepsToASide(self):
        aChessBoard = NewGameChessBoard()

        aKnight = aChessBoard.pieceAt(aRow=0, aColumn=1)
        aMovement = Movement(anInitialRow=0, anInitialColumn=1, aNewRow=2, aNewColumn=4)
        aPlay = Play(aPiece=aKnight, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test17aRookCanMoveInAStraightLine(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aRookFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aRookFreeingPlay)

        aRook = aChessBoard.pieceAt(aRow=0, aColumn=0)
        aMovement = Movement(anInitialRow=0, anInitialColumn=0, aNewRow=2, aNewColumn=0)
        aPlay = Play(aPiece=aRook, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=2, aColumn=0), aRook)

    def test18aKingCanMoveInAnyDirectionOneStepAtATime(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=4)
        aMovement = Movement(anInitialRow=1, anInitialColumn=4, aNewRow=3, aNewColumn=4)
        aKingFreeingPlay = Play(aPiece=aPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aKingFreeingPlay)

        aKing = aChessBoard.pieceAt(aRow=0, aColumn=4)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=1, aNewColumn=4)
        aPlay = Play(aPiece=aKing, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=1, aColumn=4), aKing)

    def test20aPlayInAlgebraicNotationCanBeApplied(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=4)
        aPlayInAlgebraicNotation = AlgebraicallyNotatedPlay('e2 e4', aChessBoard)
        aChessBoard.applyAPlay(aPlayInAlgebraicNotation)

        self.assertEqual(aChessBoard.pieceAt(aRow=3, aColumn=4), aPawn)

    def test21aGameHasTwoPlayers(self):
        aChessBoard = NewGameChessBoard()
        twoPlayers = [Player(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]
        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])
        players = aChessGame.players()

        self.assertTrue(len(players) == 2)
        self.assertIsInstance(players[0], Player)
        self.assertIsInstance(players[1], Player)

    def test22aPlayHasToInvolveAPiece(self):
        aChessBoard = NewGameChessBoard()

        nothing = aChessBoard.pieceAt(aRow=3, aColumn=4)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=1, aNewColumn=4)
        with self.assertRaises(AssertionError):
            aPlay = Play(aPiece=nothing, aMovement=aMovement)

    def test23aPlayerKnowsItsPieces(self):
        aChessBoard = NewGameChessBoard()
        twoPlayers = [Player(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]
        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])
        aPlayer = aChessGame.players()[0]

        aPlayersPieces = aPlayer.pieces()

        self.assertTrue(len(aPlayersPieces) == 16)
        for piece in aPlayersPieces:
            self.assertIsInstance(piece, Piece)

        boardPieces = aChessGame.board().pieces()
        self.assertTrue(all([piece in boardPieces for piece in aPlayersPieces]))

    def test24aPawnCantMoveBackwards(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        aPawn = aChessBoard.pieceAt(aRow=3, aColumn=0)
        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=2, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test25aPawnSecondMovementCanBeTwoSpacesForward(self):
        aChessBoard = NewGameChessBoard()

        aPawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        aChessBoard.applyAPlay(aPlay)

        aPawn = aChessBoard.pieceAt(aRow=3, aColumn=0)
        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=5, aNewColumn=0)
        aPlay = Play(aPiece=aPawn, aMovement=aMovement)

        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test26aPawnCanMoveInADiagonalIfItsCapturingAnEnemysPiece(self):
        aChessBoard = NewGameChessBoard()

        aWhitePawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aWhitePawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)

        aBlackPawn = aChessBoard.pieceAt(aRow=6, aColumn=1)
        aMovement = Movement(anInitialRow=6, anInitialColumn=1, aNewRow=4, aNewColumn=1)
        aPlay = Play(aPiece=aBlackPawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)

        aMovement = Movement(anInitialRow=3, anInitialColumn=0, aNewRow=4, aNewColumn=1)
        aPlay = Play(aPiece=aWhitePawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)

        self.assertTrue(aChessBoard.pieceAt(4, 1) is aWhitePawn)

    def test27aPieceCannotCaptureApieceFromItsSameTeam(self):
        aChessBoard = NewGameChessBoard()

        aRook = aChessBoard.pieceAt(aRow=0, aColumn=0)
        aMovement = Movement(anInitialRow=0, anInitialColumn=0, aNewRow=1, aNewColumn=0)
        aPlay = Play(aPiece=aRook, aMovement=aMovement)
        with self.assertRaises(InvalidMovementError):
            aChessBoard.applyAPlay(aPlay)

    def test28aPlayIsOnlyAppliedWhenThePieceMovedIsFromTheOwner(self):
        aChessBoard = NewGameChessBoard()

        whitePlayer = Player(aChessBoard.whitePieces())
        blackPlayer = Player(aChessBoard.blackPieces())

        aWhitePawn = aChessBoard.pieceAt(aRow=1, aColumn=0)
        aMovement = Movement(anInitialRow=1, anInitialColumn=0, aNewRow=3, aNewColumn=0)
        aPlay = Play(aPiece=aWhitePawn, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)
        whitePlayer._assertPlayIsValid(aPlay)
        with self.assertRaises(Exception):
            blackPlayer._assertPlayIsValid(aPlay)

        aBlackPawn = aChessBoard.pieceAt(aRow=6, aColumn=1)
        aMovement = Movement(anInitialRow=6, anInitialColumn=1, aNewRow=4, aNewColumn=1)
        aPlay = Play(aPiece=aBlackPawn, aMovement=aMovement)
        blackPlayer._assertPlayIsValid(aPlay)
        with self.assertRaises(Exception):
            whitePlayer._assertPlayIsValid(aPlay)

    def test29aKingCanCastleToTheLeft(self):
        aChessBoard = NewGameChessBoard()
        aChessBoard._matrixOfPieces[0][1] = None
        aChessBoard._matrixOfPieces[0][2] = None
        aChessBoard._matrixOfPieces[0][3] = None

        aWhiteKing = aChessBoard.pieceAt(aRow=0, aColumn=4)
        aWhiteRook = aChessBoard.pieceAt(aRow=0, aColumn=0)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=0, aNewColumn=2)
        aPlay = Play(aPiece=aWhiteKing, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=0, aColumn=2), aWhiteKing)
        self.assertEqual(aChessBoard.pieceAt(aRow=0, aColumn=3), aWhiteRook)

    def test30aKingCanCastleToTheRight(self):
        aChessBoard = NewGameChessBoard()
        aChessBoard._matrixOfPieces[0][6] = None
        aChessBoard._matrixOfPieces[0][5] = None

        aWhiteKing = aChessBoard.pieceAt(aRow=0, aColumn=4)
        aWhiteRook = aChessBoard.pieceAt(aRow=0, aColumn=7)
        aMovement = Movement(anInitialRow=0, anInitialColumn=4, aNewRow=0, aNewColumn=6)
        aPlay = Play(aPiece=aWhiteKing, aMovement=aMovement)
        aChessBoard.applyAPlay(aPlay)

        self.assertEqual(aChessBoard.pieceAt(aRow=0, aColumn=6), aWhiteKing)
        self.assertEqual(aChessBoard.pieceAt(aRow=0, aColumn=5), aWhiteRook)

    def test31aPawnCanCrown(self):
        aChessBoard = NewGameChessBoard()

        for i in range(8):
            aChessBoard._matrixOfPieces[i][0] = None

        aWhitePawn = aChessBoard.pieceAt(aRow=1, aColumn=1)
        aChessBoard._matrixOfPieces[6][0] = aWhitePawn

        class FakeNextPlayer(Player):
            def nextPlay(self, aChessBoard):
                aWhitePawn = aChessBoard.pieceAt(aRow=1, aColumn=1)
                aMovement = Movement(anInitialRow=6, anInitialColumn=0, aNewRow=7, aNewColumn=0)
                return Play(aPiece=aWhitePawn, aMovement=aMovement)

            def chooseNewRankForPawn(self, aPawn):
                return Queen(aPawn.isWhite())

        twoPlayers = [FakeNextPlayer(aChessBoard.whitePieces()), Player(aChessBoard.blackPieces())]

        aChessGame = ChessGame(aChessBoard, twoPlayers[0], twoPlayers[1])
        aChessGame._doGameStep()

        self.assertTrue(aChessGame.board().pieceAt(aRow=7, aColumn=0).isWhite())
        self.assertIsInstance(aChessGame.board().pieceAt(aRow=7, aColumn=0), Queen)
