from game.movements.invalidMovementError import InvalidMovementError


class Movement(object):
	def __init__(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
		if anInitialRow == aNewRow and anInitialColumn == aNewColumn:
			raise InvalidMovementError

		self._anInitialRow = anInitialRow
		self._anInitialColumn = anInitialColumn
		self._aNewRow = aNewRow
		self._aNewColumn = aNewColumn

	def initialRow(self):
		return self._anInitialRow

	def newRow(self):
		return self._aNewRow

	def initialColumn(self):
		return self._anInitialColumn

	def newColumn(self):
		return self._aNewColumn

	def path(self):
		path = [(self._anInitialRow, self._anInitialColumn)]
		while path[-1] != (self._aNewRow, self._aNewColumn):
			newRow = path[-1][0] + self._direction(path[-1][0], self._aNewRow)
			newColumn = path[-1][1] + self._direction(path[-1][1], self._aNewColumn)
			path.append((newRow, newColumn))
		return path

	def _direction(self, anStartingPoint, aFinishPoint):
		gradient = 0
		if anStartingPoint != aFinishPoint:
			gradient = aFinishPoint - anStartingPoint
			gradient = int(gradient / abs(gradient))
		return gradient