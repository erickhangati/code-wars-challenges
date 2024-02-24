def xo(s):
    """
    Check to see if a string has the same amount of 'x's and 'o's.
    :param s: type - str
    :return: type - boolean
    """
    string_lower = s.lower()

    x_count = 0
    y_count = 0

    for letter in string_lower:
        if letter.lower() == "x":
            x_count += 1
        elif letter.lower() == "o":
            y_count += 1


    return x_count == y_count


result = xo("zzoo")
print(result)
