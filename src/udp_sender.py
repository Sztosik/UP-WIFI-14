import socket

from .task import Task

UDP_PORT = 5005

class SenderTask(Task):
    def __init__(self, target_ip):
        super().__init__()
        self.target_ip = target_ip
        print("UDP target IP: %s" % target_ip)
        print("UDP target port: %s \n" % UDP_PORT)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP

    def _run(self) -> None:
        while True:
            msg = bytes(input("Wpisz wiadomość: "), "utf-8")
            self.sock.sendto(msg, (self.target_ip, UDP_PORT))


if __name__ == "__main__":
    sender_task = SenderTask()
    sender_task.start()
