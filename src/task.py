import threading
import time
from abc import ABC, abstractmethod


class Task(ABC):
    """ "Abstract task, all of our tasks will inherit from it"""

    def __init__(self) -> None:
        self.task_end = threading.Event()

        self.task_thread = threading.Thread(
            name=self.__class__.__name__,
            target=self._run_thread_function,
        )

    def start(self) -> None:
        self.task_thread.start()

    def stop(self) -> None:
        self.task_end.set()
        self.task_thread.join()

    def _run_thread_function(self) -> None:
        self._run()

        while True:
            if self.task_end.is_set():
                return
            time.sleep(1)

    @abstractmethod
    def _run(self) -> None:
        pass
