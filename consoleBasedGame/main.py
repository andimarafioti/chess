from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.chessGame import ChessGame

aChessGame = ChessGame()

print(aChessGame.board())
while not aChessGame.isFinished():
	userInput = raw_input('Insert next movement in Algebraic Notation --> ')
	aPlayInAlgebraicNotation = AlgebraicallyNotatedPlay(userInput, aChessGame)
	aChessGame.applyAPlay(aPlayInAlgebraicNotation)
	print(aChessGame.board())
