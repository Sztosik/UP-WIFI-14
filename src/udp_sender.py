import socket

from task import Task

UDP_IP = "192.168.1.101"
UDP_PORT = 5005
MESSAGE = b"Siemano"


class SenderTask(Task):
    def __init__(self):
        super().__init__()
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s" % UDP_PORT)
        print("message: %s" % MESSAGE)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP

    def _run(self) -> None:
        while True:
            msg = bytes(input("Wpisz wiadomość: "))
            self.sock.sendto(msg, (UDP_IP, UDP_PORT))

if __name__ == "__main__":
    sender_task = SenderTask()
    sender_task.start()

#print("UDP target IP: %s" % UDP_IP)
#print("UDP target port: %s" % UDP_PORT)
#print("message: %s" % MESSAGE)

#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
#sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
