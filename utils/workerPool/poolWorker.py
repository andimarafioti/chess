import logging
import traceback
from threading import Thread, current_thread

from utils.workerPool.task import StopWorkerTask

__author__ = 'Jules'


class PoolWorker(Thread):
	STOP_TASK = StopWorkerTask()

	def __init__(self, owner):
		super(PoolWorker, self).__init__()

		self.setDaemon(True)
		self._owner = owner
		self._tasksQueue = owner.tasks()
		self._canceledTasks = owner.canceledTasks()
		self._logger = self._owner.logger()

	def owner(self):
		return self._owner

	def run(self):
		self._logger.info("PoolWorker <%s> started.", current_thread().ident)
		while True:
			task = self._tasksQueue.get(block=True)

			if task is PoolWorker.STOP_TASK:
				self._tasksQueue.task_done()
				self._logger.info("PoolWorker task stopped, empty: %s", self._tasksQueue.empty())
				break

			if task in self._canceledTasks:
				self._canceledTasks.remove(task)
				self._tasksQueue.task_done()
				self._logger.debug("PoolWorker <%s> canceled call: %s%s", current_thread().ident, task._function.__name__,
							 str(task._argTuple))
				continue

			self._logger.debug("PoolWorker <%s> is about to call: %s%s", current_thread().ident, task._function.__name__,
						 str(task._argTuple))

			try:
				task.run()
			except Exception, e:
				self._logger.error("PoolWorker <%s> catched an exception calling: %s%s", current_thread().ident,
							   task._function, str(task._function))
				self._logger.exception(e)

			self._logger.debug("PoolWorker <%s> called: %s%s", current_thread().ident, task._function.__name__,
						 str(task._argTuple))

			self._tasksQueue.task_done()

		self._logger.warning("PoolWorker <%s> STOPPED", current_thread().ident)
