def positive_sum(arr):
    """
    Calculate sum of positive numbers.
    :param arr: type - list
    :return: type - num
    """
    filtered_arr = [number for number in arr if number > 0]
    return sum(filtered_arr)


result = positive_sum([1, -4, 7, 12])
print(result)