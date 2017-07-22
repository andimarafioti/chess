import sys

from utils.subject import Subject

isTesting = "unittest" in sys.modules.keys()


class Model(object):
	SHOW_VIEW = 0
	CLOSE_VIEW = 1

	def __init__(self, parent=None):
		self._parent = parent

		self.subject = Subject(self)

		self.presenter = self._getPresenterInstance()

	def accept(self, visitor):
		return visitor.visitModel(self)

	def parent(self):
		return self._parent

	def close(self):
		self.subject.notify(Model.CLOSE_VIEW)

	def closeModel(self):
		self.subject.clearObservers()

	def showView(self):
		self.subject.notify(Model.SHOW_VIEW)

	def onViewClosed(self):
		self.presenter = None

	def _getPresenterInstance(self):
		raise NotImplementedError("Subclass responsibility")

	def onNotify(self, emitter, event, args):
		pass
