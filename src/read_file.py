from copy import deepcopy

from .task import Task

CHUNK_SIZE = 16


chunk_list: list[bytearray] = []

with open("example_file.txt", mode="rb") as f:
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
    chunk_list.append(deepcopy(chunk))


for chunk in chunk_list:
    print(chunk)
