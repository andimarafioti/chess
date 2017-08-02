class Play(object):
	def __init__(self, aPiece, aMovement):
		self._aPiece = aPiece
		self._aMovement = aMovement

	def piece(self):
		return self._aPiece

	def movement(self):
		return self._aMovement

	def initialRow(self):
		return self._aMovement.initialRow()

	def newRow(self):
		return self._aMovement.newRow()

	def initialColumn(self):
		return self._aMovement.initialColumn()

	def newColumn(self):
		return self._aMovement.newColumn()
