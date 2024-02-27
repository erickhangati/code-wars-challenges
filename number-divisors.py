def divisors(n):
    """
    Count the number of divisors of n.
    :param n: type - number
    :return: type - number
    """
    count = 0

    for i in range(1, n + 1):
        if n % i == 0:
            count += 1

    return count


result = divisors(12)
print(result)
