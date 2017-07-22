# coding=utf-8
from PySide.QtCore import Signal, Qt
from PySide.QtGui import QWidget


class View(QWidget):
	Show = Signal()
	Close = Signal()
	Hide = Signal()

	def __init__(self, presenter, parent=None):
		super(View, self).__init__(parent=parent)
		self.setAttribute(Qt.WA_DeleteOnClose, False)

		self.presenter = presenter

		self.Show.connect(self.show, Qt.QueuedConnection)
		self.Hide.connect(self.hide, Qt.QueuedConnection)
		self.Close.connect(self.close, Qt.QueuedConnection)

	def closeEvent(self, event):
		self.presenter.onViewClosed()
		self.presenter = None
		super(View, self).closeEvent(event)
