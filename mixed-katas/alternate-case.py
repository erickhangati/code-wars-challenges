def to_alternating_case(string):
    """
    Convert letter to alternate case
    :param string: type - str
    :return: type - str
    """
    return string.swapcase()
    # return ''.join([letter.upper() if letter.islower() else letter.lower() for letter in string])


result = to_alternating_case("HeLLo WoRLD")
print(result)
