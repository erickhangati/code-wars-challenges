def area_or_perimeter(length, width):
    """
    If it is a square, return its area. If it is a rectangle, return its perimeter.
    :param length: type - number
    :param width: type - number
    :return: type - number
    """
    return length * width if length == width else (length + width) * 2
