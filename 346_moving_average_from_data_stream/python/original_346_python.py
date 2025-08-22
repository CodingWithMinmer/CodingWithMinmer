from queue import Queue


class MovingAverage_346:
    def __init__(self, size: int):
        self.size = size
        self.queue = Queue()
        self.window_sum = 0

    def next(self, val: int) -> float:
        self.window_sum += val
        self.queue.put(val)

        if self.queue.qsize() > self.size:
            self.window_sum -= self.queue.get()

        return self.window_sum / self.queue.qsize()
