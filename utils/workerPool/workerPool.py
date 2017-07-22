import logging
from _weakrefset import WeakSet

from utils.workerPool.fifoPriorityQueue import FIFOPriorityQueue
from utils.workerPool.poolWorker import PoolWorker
from utils.workerPool.task import Task

__author__ = 'Jules'

# logger = logging.getLogger('[WORKER POOL]')
# logger.setLevel(logging.INFO)


class WorkerPool(object):
	def __init__(self, name, poolSize=4, loggingLevel=logging.INFO):
		super(WorkerPool, self).__init__()

		self._logger = logging.getLogger("[WORKER POOL - {}]".format(name.upper()))
		self._logger.setLevel(loggingLevel)

		self._name = name
		self._isRunning = False

		self._tasksQueue = FIFOPriorityQueue()
		self._canceledTasks = WeakSet()
		self._workers = [PoolWorker(self) for _ in range(poolSize)]

	def name(self):
		return self._name

	def logger(self):
		return self._logger

	def tasks(self):
		return self._tasksQueue

	def canceledTasks(self):
		return self._canceledTasks

	def start(self):
		self._logger.info("Starting...")

		for worker in self._workers:
			worker.start()

		self._isRunning = True

		self._logger.info("Started.")

	def stop(self):
		self._logger.info("Stopping WorkerPool ...")

		if not self._isRunning:
			self._logger.warning("Attempted to stop a WorkerPool twice.")
			return

		for _ in range(len(self._workers)):
			self._tasksQueue.put((5, PoolWorker.STOP_TASK))

		self._isRunning = False

		self._tasksQueue.join()

		self._logger.info("WorkerPool stopped.")

	def join(self):
		self._logger.info("Waiting for tasks to be done...")
		self._tasksQueue.join()
		self._logger.info("Tasks done!")

	def addTask(self, function, *args):
		if not self._isRunning:
			self._logger.debug("Task not added to (stopped) queue: %s%s.", function.__name__, str(args))
			return

		self._logger.debug("Adding task to queue: %s%s.", function.__name__, str(args))
		task = Task(function, args)
		self._tasksQueue.put((3, task))

		return task

	def addHighPriorityTask(self, function, *args):
		if not self._isRunning:
			self._logger.debug("HIGH PRIORITY task not added to (stopped) queue: %s%s.", function.__name__, str(args))
			return

		self._logger.debug("Adding HIGH PRIORITY task to queue: %s%s.", function.__name__, str(args))
		task = Task(function, args)
		self._tasksQueue.put((0, task))

		return task

	def addLowPriorityTask(self, function, *args):
		if not self._isRunning:
			self._logger.debug("LOW PRIRITY task not added to (stopped) queue: %s%s.", function.__name__, str(args))
			return

		self._logger.debug("Adding LOW PRIORITY task to queue: %s%s.", function.__name__, str(args))
		task = Task(function, args)

		self._tasksQueue.put((4, task))

		return task

	def cancelTask(self, task):
		self._logger.debug("Adding CANCELLATION for task: %s%s.", task._function.__name__, str(task._argTuple))
		self._canceledTasks.add(task)

	def isRunning(self):
		return self._isRunning

