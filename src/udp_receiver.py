import socket

from .merge_chunks import merge_chunks
from .task import Task

UDP_PORT = 5005


class ReceiverTask(Task):
    def __init__(self):
        super().__init__()
        self.file_transmission = False
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP
        self.sock.bind(("0.0.0.0", UDP_PORT))

    def _run(self) -> None:
        while True:
            data, addr = self.sock.recvfrom(1024)  # buffer size is 1024 bytes
            if "!start" in str(data):
                print("---> rozpoczęto przesyłanie pliku")
                received_data = []
                while True:
                    data, addr = self.sock.recvfrom(1024)
                    if "!stop" in str(data):
                        break
                    received_data.append(data)
                print("---> zakończono przesyłanie pliku")

                file_name = input("Nazwa pliku do zapisania: ")
                merge_chunks(received_data, file_name)
                print("zapisano plik")
            else:
                print("-> %s" % str(data)[2:-1])
