from _weakrefset import WeakSet
from threading import Event, current_thread
from unittest import TestCase

from mock import Mock

from utils.workerPool.fifoPriorityQueue import FIFOPriorityQueue
from utils.workerPool.poolWorker import PoolWorker
from utils.workerPool.task import Task
from utils.workerPool.workerPool import WorkerPool

__author__ = 'Jules'


class TestPoolWorker(TestCase):
	def setUp(self):
		self.workerPool = Mock(WorkerPool)
		self.workerPool.name.return_value = "Test WorkerPool"
		self.workerPool.tasks.return_value = FIFOPriorityQueue()
		self.workerPool.canceledTasks.return_value = WeakSet()
		self.poolWorker = PoolWorker(self.workerPool)

	def tearDown(self):
		self.workerPool.tasks().put((1, PoolWorker.STOP_TASK))

	def testWorkersStayAliveEvenIfTaskRaisesAnException(self):
		taskDoneEvent = Event()

		def setTaskDone():
			taskDoneEvent.set()

		def raiseException():
			raise Exception("Foo")

		self.poolWorker.start()

		self.workerPool.tasks().put((1, Task(raiseException)))
		self.workerPool.tasks().put((1, Task(setTaskDone)))

		workerKeptWorking = taskDoneEvent.wait(1)

		self.assertTrue(self.poolWorker.isAlive())
		self.assertTrue(workerKeptWorking)

	def testWorkersRunTasksFromTheirQueue(self):
		taskDoneEvent = Event()

		def setTaskDone():
			taskDoneEvent.set()

		self.poolWorker.start()

		self.workerPool.tasks().put((1, Task(setTaskDone)))

		taskDone = taskDoneEvent.wait(1)

		self.assertTrue(taskDone)

	def testWorkerThreadsRunAsDaemons(self):
		global isRunningAsDaemon
		isRunningAsDaemon = False

		def setIsRunningAsDaemon():
			global isRunningAsDaemon
			isRunningAsDaemon = current_thread().isDaemon()

		self.poolWorker.start()

		self.workerPool.tasks().put((1, Task(setIsRunningAsDaemon)))
		self.workerPool.tasks().join()

		self.assertTrue(isRunningAsDaemon)

	def testWorkersStopRunningWhenSTOP_TASKIsQueued(self):
		self.poolWorker.start()

		self.workerPool.tasks().put((1, PoolWorker.STOP_TASK))

		self.poolWorker.join(1)

		self.assertFalse(self.poolWorker.isAlive())

	def testWorkersDontStartRunningUntilToldTo(self):
		self.assertFalse(self.poolWorker.isAlive())

		self.poolWorker.start()

		self.assertTrue(self.poolWorker.isAlive())
