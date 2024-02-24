def digitize(n):
    """
    Converts a number to a reversed list.
    :param n: type - int
    :return: reversed list
    """
    if n < 0:
        return

    # Reverse number and convert to string
    reversed_nums = str(n)[::-1]
    reversed_list = []

    # Loop string
    for letter in reversed_nums:
        reversed_list.append(int(letter))

    return reversed_list


# Alternative solution
def digitize_1(n):
    """
    Converts a number to a reversed list.
    :param n: type - int
    :return: reversed list
    """
    return [int(num) for num in str(n)[::-1]]
