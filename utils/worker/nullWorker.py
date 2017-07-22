from utils.worker.worker import Worker


class NullWorker(Worker):
	def __init__(self):
		super(NullWorker, self).__init__()

	def stop(self):
		pass