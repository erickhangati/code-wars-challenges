def stray(arr):
    """
    Find the different item.
    :param arr: type - list
    :return: type - int
    """
    unique_arr = list(set(arr))
    return unique_arr[0] if arr.count(unique_arr[0]) == 1 else unique_arr[1]


result = stray([17, 17, 3, 17, 17, 17, 17])
print(result)
