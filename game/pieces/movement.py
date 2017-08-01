class Movement(object):
	def __init__(self, anInitialRow, anInitialColumn, aNewRow, aNewColumn):
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
