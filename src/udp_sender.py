import socket

from .task import Task

UDP_IP = "192.168.1.101"
UDP_PORT = 5005


class SenderTask(Task):
    def __init__(self):
        super().__init__()
        print("UDP target IP: %s" % UDP_IP)
        print("UDP target port: %s \n" % UDP_PORT)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP

    def _run(self) -> None:
        while True:
            msg = bytes(input("Wpisz wiadomość: "), "utf-8")
            self.sock.sendto(msg, (UDP_IP, UDP_PORT))


if __name__ == "__main__":
    sender_task = SenderTask()
    sender_task.start()
