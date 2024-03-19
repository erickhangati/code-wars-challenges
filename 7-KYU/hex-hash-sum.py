"""
CHALLENGE: Hex Hash Sum

Complete the function that accepts a valid string and returns an integer.

Wait, that would be too easy! Every character of the string should be converted
to the hex value of its ascii code, then the result should be the sum of the numbers
in the hex strings (ignore letters).

Examples:

"Yo" ==> "59 6f" ==> 5 + 9 + 6 = 20
"Hello, World!"  ==> 91
"Forty4Three"    ==> 113
"""


def hex_hash(code):
    hex_char = ''
    for letter in code:
        hex_char += hex(ord(letter))

    num_char = sum(int(i) for i in hex_char if i.isdigit())

    return num_char


result = hex_hash("Yo")
print(result)
