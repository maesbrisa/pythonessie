def to_string(bytes_or_string):
    if isinstance(bytes_or_string, bytes):
        string = bytes_or_string.decode('utf-8')
    else:
        string = bytes_or_string
    return string


def to_bytes(bytes_or_string):
    if isinstance(bytes_or_string,str):
        byte = bytes_or_string.encode('utf-8')
    else:
        byte = bytes_or_string
    return byte
