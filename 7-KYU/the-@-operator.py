"""
CHALLENGE: The @ operator

I invented a new operator, @, which is left associative.

a @ b = (a + b) + (a - b) + (a * b) + (a // b)

Side note: ~~ is shorthand for Math.floor.

Given a string containing only integers and the operators, find out the value of that string.

The strings will always be "well formed", meaning with a space on each side of the operators,
except in TypeScript, where string may appear like this: 0@1@2

1 @ 1 = (1 + 1) + (1 - 1) + (1 * 1) + (1 // 1) = 4
3 @ 2 = 13
6 @ 9 = 66

4 @ -4 = -9\
1 @ 1 @ -4 = -9 (1 @ 1 is 4, 4 @ -4 is -9)
2 @ 2 @ 2 = 40
0 @ 1 @ 2 = 0
5 @ 0 = None
Good luck!
"""


def evaluate(equation):
    operands = equation.split(" @ ")
    base = 0

    for i, operand in enumerate(operands):
        if i == 0:
            base = int(operand)
        elif int(operand) == 0:
            return None
        else:
            base = (base + int(operand)) + (base - int(operand)) + (base * int(operand)) + (base // int(operand))

    return base


result = evaluate('2 @ 2 @ 2')
print(result)
