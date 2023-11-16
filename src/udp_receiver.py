import socket

from .task import Task

UDP_PORT = 5005


class ReceiverTask(Task):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
        self.sock.bind(("0.0.0.0", UDP_PORT))

    def _run(self) -> None:
        while True:
            data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
            print("\n->: %s" % str(data)[2:-1])
