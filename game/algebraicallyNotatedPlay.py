from game.movements.movement import Movement
from game.play import Play


class AlgebraicallyNotatedPlay(Play):
	def __init__(self, aStringDenotingAnAlgebraicallyNotatedPlay, aChessGame):
		aSplitedStringDenotingAnAlgebraicallyNotatedPlay = aStringDenotingAnAlgebraicallyNotatedPlay.split()

		initialColumn = ord(aSplitedStringDenotingAnAlgebraicallyNotatedPlay[-2][0].lower()) - 97
		initialRow = int(aSplitedStringDenotingAnAlgebraicallyNotatedPlay[-2][1]) - 1

		newColumn = ord(aSplitedStringDenotingAnAlgebraicallyNotatedPlay[-1][0].lower()) - 97
		newRow = int(aSplitedStringDenotingAnAlgebraicallyNotatedPlay[-1][1]) - 1

		assert 2 <= len(aSplitedStringDenotingAnAlgebraicallyNotatedPlay) <= 3, "Algebraic Notation Error"
		assert all([0 <= value <= 7 for value in [initialRow, initialColumn, newRow, newColumn]]), "Movement Outside of " \
																								   "board boundaries"

		aPiece = aChessGame.pieceAt(aRow=initialRow, aColumn=initialColumn)
		aMovement = Movement(initialRow, initialColumn, newRow, newColumn)
		super(AlgebraicallyNotatedPlay, self).__init__(aPiece=aPiece, aMovement=aMovement)
