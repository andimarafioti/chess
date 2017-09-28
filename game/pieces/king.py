from game.pieces.piece import Piece


class King(Piece):
    def canApplyAMovement(self, aMovement):
        return len(aMovement.path()) == 2
    #
    # def canApplyASpecialPlay(self, aPlay):
    #     if not self.HAS_MOVED and self._isCastlingMovement(aPlay.movement()):
    #         aPlay.setSpecialPlayConsequence()
    #
    # def _isCastlingMovement(self, aMovement):
    #     return aMovement.initialRow() == aMovement.newRow() and \
    #            abs(aMovement.initialColumn() - aMovement.newColumn()) == 2
