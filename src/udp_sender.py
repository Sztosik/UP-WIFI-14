import socket
import time
from copy import deepcopy

from .task import Task

UDP_PORT = 5005
CHUNK_SIZE = 1_000


def get_chunks(file_name):
    chunk_list: list[bytearray] = []

    with open(file_name, mode="rb") as f:
        data = f.read()

        i = 0
        chunk = bytearray()
        for byte in data:
            if i == CHUNK_SIZE:
                chunk_list.append(deepcopy(chunk))
                chunk = bytearray()
                i = 0
            chunk.append(byte)
            i += 1
        if i != 0:
            chunk_list.append(deepcopy(chunk))

    return chunk_list


class SenderTask(Task):
    def __init__(self, target_ip):
        super().__init__()
        self.target_ip = target_ip
        print("UDP target IP: %s" % target_ip)
        print("UDP target port: %s \n" % UDP_PORT)

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Internet  # UDP

        print("ZACZNIJ PISAĆ:\n")

    def _run(self) -> None:
        while True:
            command = input()
            msg = bytes(command, "utf-8")
            if "!file" in command:
                name = input("Podaj nazwe pliku: ")
                chunks = get_chunks(name)

                self.sock.sendto(b"!start", (self.target_ip, UDP_PORT))

                for chunk in chunks:
                    time.sleep(0.01)
                    self.sock.sendto(chunk, (self.target_ip, UDP_PORT))

                self.sock.sendto(b"!stop", (self.target_ip, UDP_PORT))
                print("Plik został wysłany")
            else:
                self.sock.sendto(msg, (self.target_ip, UDP_PORT))


if __name__ == "__main__":
    sender_task = SenderTask()
    sender_task.start()
