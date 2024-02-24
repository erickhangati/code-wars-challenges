def basic_op(operator, value1, value2):
    """
    Calculating basic mathematics operations.
    :param operator: type - str
    :param value1: type - num
    :param value2: type - num
    :return: type - num
    """

    if operator == "+":
        return value1 + value2
    elif operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2

    # Another alternative
    # return eval(f"{value1}{operator}{value2}")


result = basic_op("+", 1, 2)
print(result)
