def accum(st):
    """
    Form an accumulated string.
    :param st: type - str
    :return: type - str
    """
    accum_str = [(letter*(i+1)).capitalize() for i, letter in enumerate(st)]

    # for i, letter in enumerate(st):
    #     accum_str.append((letter * (i + 1)).capitalize())

    return "-".join(accum_str)


result = accum("zzoo")
print(result)
