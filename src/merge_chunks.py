def merge_chunks(chunk_list, output_file):
    file_data = bytearray()
    for chunk in chunk_list:
        for byte in chunk:
            file_data.append(byte)

    file = open(f"{output_file}", "wb")
    file.write(file_data)
    file.close()