def check_if_length_exceeds(object, max_length):
    if len(object) > max_length:
        raise Exception("This object has exceeded the maximum size")


def check_if_length_equals(object, length):
    if len(object) != length:
        raise Exception("This object has an incorrect length")