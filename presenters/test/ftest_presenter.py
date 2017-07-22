from unittest import TestCase

from mock import Mock, patch

from models.model import Model
from presenters.presenter import Presenter


class TestPresenter(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.threading_event_patcher = patch('threading.Event')
		cls.threading_event_patcher.start()
		cls.presentersCreateView = patch('presenters.presenter.Presenter.CreateView')
		cls.presentersCreateView.start()
		cls.QApplicationsInstance = patch('PySide.QtGui.QApplication.instance')
		cls.QApplicationsInstance.start()
		cls.QObjectsMoveToThread = patch('PySide.QtCore.QObject.moveToThread')
		cls.QObjectsMoveToThread.start()

	@classmethod
	def tearDownClass(cls):
		cls.threading_event_patcher.stop()
		cls.presentersCreateView.stop()
		cls.QApplicationsInstance.stop()
		cls.QObjectsMoveToThread.stop()

	def setUp(self):
		model = Mock()

		self.presenter = Presenter(model)

	def tearDown(self):
		pass

	def testWhenModelNotifiesSHOW_VIEWViewCallsShowView(self):
		view = Mock()
		self.presenter.view = view
		self.presenter.onNotify(self.presenter.model, Model.SHOW_VIEW, ())
		view.Show.emit.assert_called_with()

	def testWhenInstantiatedThenPresentersCreateViewsInUIThread(self):
		self.presenter.CreateView.emit.assert_called_with()
