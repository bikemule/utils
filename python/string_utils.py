'''Stupid Python tricks. Hopefully useful at some point.'''

def str_with_leading_zeros(num_to_convert, min_length):
    """Converts a number to a string and left-pads it with 0s to at least
    min_length. Probably a better, more Pythonic, std lib way."""

    s = str(num_to_convert)

    if len(s) < min_length:
        s = "0" * (min_length - len(s)) + s

    return s

