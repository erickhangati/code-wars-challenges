def square_digits(num):
    """
    Square digits of a number
    :param num: type - num
    :return: type - num
    """
    square_digits_list = [str(int(digit)**2) for digit in str(num)]
    join_nums = int(''.join(square_digits_list))
    return join_nums


results = square_digits(9119)
print(results)
