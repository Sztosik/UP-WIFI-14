import socket

from .task import Task

UDP_IP = "192.168.1.101"
UDP_PORT = 5005


class ReceiverTask(Task):
    def __init__(self):
        super().__init__()
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
        self.sock.bind((UDP_IP, UDP_PORT))

    def _run(self) -> None:
        while True:
            data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
            print("received message: %s" % str(data))


#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
#sock.bind((UDP_IP, UDP_PORT))

#while True:
    #data, addr = sock.recvfrom(1024)  # buffer size is 1024 bytes
    #print("received message: %s" % str(data))