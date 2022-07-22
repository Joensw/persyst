def byte_to_nibble_list(byte_val):
    return list([byte_val >> 4 & 0x0F, byte_val & 0x0F])


def read_all_bytes(source):
    file = open(source, "rb")
    return file.read()


def read_nibbles(source):
    byte_list = read_all_bytes(source)
    nibble_list = []
    for byte in byte_list:
        nibble_list.extend(byte_to_nibble_list(byte))
    return nibble_list


def write_bytes(target, content):
    bytes_input = b''.join(content)
    file = open(target, "wb")
    file.write(bytes_input)
    file.close()
