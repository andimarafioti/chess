from threading import current_thread
from time import sleep
from unittest import TestCase
from utils.worker.worker import Worker


class TestWorker(TestCase):

    def testWorkerCallsFunctionsWithNoParameters(self):
        global functionWasCalled

        functionWasCalled = False

        def setFunctionWasCalledToTrue():
            global functionWasCalled
            functionWasCalled = True

        self.assertFalse(functionWasCalled)

        Worker.call(setFunctionWasCalledToTrue).asDaemon.start().join()

        self.assertTrue(functionWasCalled)

    def testWorkerCallsFunctionsWithPassedParameters(self):
        global functionWasCalled

        functionWasCalled = False

        def setFunctionWasCalledTo(boolean):
            global functionWasCalled
            functionWasCalled = boolean

        self.assertFalse(functionWasCalled)

        Worker.call(setFunctionWasCalledTo).withArgs(True).asDaemon.start().join()

        self.assertTrue(functionWasCalled)

    def testWorkerCallsFunctionsInAnotherThread(self):
        global workerThread

        workerThread = None

        def setworkerThread():
            global workerThread
            workerThread = current_thread()

        Worker.call(setworkerThread).asDaemon.start().join()

        self.assertIsNotNone(workerThread)
        self.assertFalse(current_thread() == workerThread)

    def testIfWorkerIsSetAsDaemonThenCallsFunctionsInADaemonThread(self):
        global workerThreadIsDaemon

        workerThreadIsDaemon = False

        def setWorkerThreadIsDaemon():
            global workerThreadIsDaemon
            workerThreadIsDaemon = current_thread().isDaemon()

        worker = Worker.call(setWorkerThreadIsDaemon).asDaemon.start()

        worker.join()

        self.assertTrue(workerThreadIsDaemon)

    def testIfWorkerThreadIsNotSetDaemonThenCallsFunctionsInANonDaemonThread(self):
        global workerThreadIsDaemon

        workerThreadIsDaemon = False

        def setWorkerThreadIsDaemon():
            global workerThreadIsDaemon
            workerThreadIsDaemon = current_thread().isDaemon()

        Worker.call(setWorkerThreadIsDaemon).start().join()

        self.assertFalse(workerThreadIsDaemon)

    def testJoiningAWorkerWaitsUntilWorkIsDone(self):
        global workDone

        workDone = False

        def sleepOneSecondAndSetWorkDoneToTrue():
            global workDone
            sleep(0.1)
            workDone = True

        Worker.call(sleepOneSecondAndSetWorkDoneToTrue).asDaemon.start().join()

        self.assertTrue(workDone)

    def testWorkerKnowsWhenItIsWorking(self):
        worker = Worker.call(sleep).withArgs(0.1).asDaemon.start()

        self.assertTrue(worker.isWorking())

    # def testWorkerAlwaysUsesTheSameThread(self):
    #     global workerThread
    #     workerThread = None
	#
    #     def setWorkerThread():
    #         global workerThread
    #         workerThread = current_thread()
	#
    #     worker = Worker.call(setWorkerThread).asDaemon.start().join()
	#
    #     self.assertIsNotNone(workerThread)
	#
    #     firstWorkerThread = workerThread
	#
    #     worker.start().join()
	#
    #     secondWorkerThread = workerThread
	#
    #     self.assertTrue(firstWorkerThread == secondWorkerThread)
