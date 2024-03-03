"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""


def remove_exclamation_marks(s):
    return ''.join([letter for letter in s if letter != "!"])


result = remove_exclamation_marks("E!r!i!c")
print(result)
