from unittest import TestCase

from mock import Mock, patch

from models.model import Model


class TestModel(TestCase):
	@classmethod
	def setUpClass(cls):
		cls.modelGetPresenterInstancePatch = patch('models.model.Model._getPresenterInstance')
		cls.modelGetPresenterInstanceClass = cls.modelGetPresenterInstancePatch.start()

	# noinspection PyUnresolvedReferences
	@classmethod
	def tearDownClass(cls):
		cls.modelGetPresenterInstancePatch.stop()

	def setUp(self):
		if self.__class__ is not TestModel:
			return

		self.modelGetPresenterInstanceClass.reset_mock()

		self.model = Model()

	def testWhenShowViewCalledNotifySHOW_VIEW(self):
		observer = Mock()
		self.model.subject.addObserver(observer)
		self.model.showView()
		observer.onNotify.assert_called_with(self.model, Model.SHOW_VIEW, ())
