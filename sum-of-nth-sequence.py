"""
Your task is to write a function which returns the sum of following series up to nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:
You need to round the answer to 2 decimal places and return it as String.

If the given value is 0 then it should return 0.00

You will only be given Natural Numbers as arguments.

Examples:(Input --> Output)
1 --> 1 --> "1.00"
2 --> 1 + 1/4 --> "1.25"
5 --> 1 + 1/4 + 1/7 + 1/10 + 1/13 --> "1.57"
"""


def series_sum(n):
    base = 1
    fraction = 4
    cumulated_fraction = 0

    if isinstance(n, str) or n == 0:
        return "0.00"
    elif n == 1:
        return "{:.2f}".format(float(base))
    else:
        for num in range(2, n + 1):
            cumulated_fraction += 1 / fraction
            fraction += 3

    return "{:.2f}".format(round(base + cumulated_fraction, 2))


result = series_sum(2)
print(result)
