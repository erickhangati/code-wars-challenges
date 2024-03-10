"""
CHALLENGE: Sum the Repeats

Write a function that takes a list comprised of other lists of integers and returns the sum of all numbers that appear in two or more lists in the input list. Now that might have sounded confusing, it isn't:

repeat_sum([[1, 2, 3],[2, 8, 9],[7, 123, 8]])
sum of [2, 8]
return 10

repeat_sum([[1], [2], [3, 4, 4, 4], [123456789]])
sum of []
return 0

repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
sum of [1,8]
return 9
"""


def repeat_sum(list_items):
    nums = set(item for row in list_items for item in row)
    repeats = []
    checked = []

    for num in nums:
        for item_1 in list_items:
            if num in item_1 and num in checked and num not in repeats:
                repeats.append(num)
            elif num in item_1 and num not in checked:
                checked.append(num)

    return sum(repeats)


result = repeat_sum([[1, 8, 8], [8, 8, 8], [8, 8, 8, 1]])
print(result)
