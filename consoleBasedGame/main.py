from game.algebraicallyNotatedPlay import AlgebraicallyNotatedPlay
from game.chessGame import ChessGame

aChessGame = ChessGame()
isFinished = False
print(aChessGame.board())

while not isFinished:
	userInput = input('Insert next movement in Algebraic Notation --> ')
	aPlayInAlgebraicNotation = AlgebraicallyNotatedPlay(userInput, aChessGame)
	aChessGame.applyAPlay(aPlayInAlgebraicNotation)
	print(aChessGame.board())
