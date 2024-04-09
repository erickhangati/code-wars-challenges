"""
Shortest Word

Simple, given a string of words, return the length of the shortest word(s).

String will never be empty, and you do not need to account for different data types.
"""


def find_short(s):
    length = len(s)

    for word in s.split(" "):
        if len(word) < length:
            length = len(word)

    return length


res = find_short("eric is min")
print(res)
