def number(bus_stops):
    """
    Count the number of passengers remaining.
    :param bus_stops: list of items with picked up and drop passengers.
    :return: number of remaining passengers.
    """
    picked = 0
    dropped = 0

    for stop in bus_stops:
        picked += stop[0]
        dropped += stop[1]

    return picked - dropped


result = number([[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]])
print(result)
