def points(games):
    """
    Calculate football championship scores.
    :param games:
    :return:
    """
    count = 0

    for scores in games:
        split_scores = scores.split(":")
        if int(split_scores[0]) > int(split_scores[1]):
            count += 3
        elif int(split_scores[0]) == int(split_scores[1]):
            count += 1

    return count


result = points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3'])
print(result)
