# -*- coding: utf-8 -*-
import logging
from _weakrefset import WeakSet
from threading import RLock


def stringFor(something):
	# TODO: something smart
	return str(something)


class Subject(object):
	def __init__(self, parent, loggingLevel=logging.INFO):
		super(Subject, self).__init__()

		self._logger = logging.getLogger("[OBSERVER {} ({})]".format(parent.__class__.__name__.upper(), id(parent)))
		self._logger.setLevel(loggingLevel)

		self.parent = parent
		self._observers_lock = RLock()
		self._observers = WeakSet()

	def addObserver(self, observer):
		with self._observers_lock:
			self._observers.add(observer)

		self._logger.debug("%s is being observed by %s", stringFor(self.parent), stringFor(observer))

	def removeObserver(self, observer):
		with self._observers_lock:
			try:
				self._observers.remove(observer)
			except KeyError:
				self._logger.error("Tried to remove observer %s twice from %s", stringFor(observer),
								   stringFor(self.parent))

	def hasObserver(self, observer):
		with self._observers_lock:
			return observer in self._observers

	def clearObservers(self):
		with self._observers_lock:
			self._observers.clear()

		self._logger.debug("%s observers were cleaned.", stringFor(self.parent))

	def notify(self, event, *args):
		with self._observers_lock:
			observers = list(self._observers)

		for obs in observers:
			self._logger.debug("%s is about to notify %s to %s", stringFor(self.parent), event, stringFor(obs))
			try:
				obs.onNotify(self.parent, event, args)
			except Exception as e:
				self._logger.error("Catched exception trying to notify %s to %s with arguments: %s",
								   str(event),
								   str(obs),
								   str(args))
				self._logger.exception(e)
