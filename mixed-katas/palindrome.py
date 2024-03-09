def is_palindrome(s):
    """
    Check if palindrome
    :param s: type - str
    :return: boolean
    """
    s_lower = s.lower()
    return s_lower == s_lower[::-1]


results = is_palindrome("madam")
print(results)
