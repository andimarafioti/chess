import threading

from utils.worker.worker import Worker

__author__ = 'Dev6'


class DeferredWorker(Worker):
	def __init__(self):
		super(DeferredWorker, self).__init__()
		self._waitTime = 0
		self._isCanceled = False
		self._isDead = False

		self._lock = threading.RLock()

	@staticmethod
	def fromWorker(worker):
		deferredWorker = DeferredWorker()

		deferredWorker._thread = worker._thread
		deferredWorker._isDaemon = worker._isDaemon
		deferredWorker._function = worker._function
		deferredWorker._arguments = worker._arguments

		return deferredWorker

	def after(self, seconds):
		self._waitTime = seconds
		return self

	def setWaitTime(self, seconds):
		with self._lock:
			self._waitTime
		return self

	def start(self):
		with self._lock:
			if self._isDead:
				return self

			if self._thread:
				self._thread.cancel()

			self._thread = threading.Timer(self._waitTime, function=self._function, args=self._arguments)
			self._thread.daemon = self._isDaemon
			self._thread.start()

		return self

	def stop(self):
		with self._lock:
			self._isCanceled = True

			if self._thread:
				self._thread.cancel()

		return self

	def kill(self):
		with self._lock:
			self.stop()
			self._isDead = True

	def isCanceled(self):
		return self._isCanceled