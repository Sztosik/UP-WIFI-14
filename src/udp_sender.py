import socket

from task import Task

UDP_IP = "192.168.1.101"
UDP_PORT = 5005
MESSAGE = b"Siemano"


class SenderTask(Task):
    def __init__(self):
        super().__init__()

    def _run(self) -> None:
        while True:
            # write your code here
            pass


print("UDP target IP: %s" % UDP_IP)
print("UDP target port: %s" % UDP_PORT)
print("message: %s" % MESSAGE)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
