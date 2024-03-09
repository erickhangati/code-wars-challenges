"""
CHALLENGE: Average Fuel Consumption

Story
You just returned from a car trip, and you are curious about your fuel consumption during the trip.
Unfortunately, you didn't reset the counter before you started, but you have written down the average
consumption of the car and the previous distance travelled at that time. Looking at the dashboard, you
note the current data...

Task
Complete the function that receives two pairs of input (before, after), and return the calculated average
fuel consumption of your car during your trip, rounded to 1 decimal.

Both pairs consist of 2 valid numbers:

the average consumption of the car (l/100km, float)
the previous distance travelled (km, integer)

Examples:

      BEFORE                   AFTER                  DURING
avg. cons, distance     avg. cons, distance         avg. cons
[l/100km]    [km]       [l/100km]    [km]           [l/100km]

[   7.9  ,   100  ]  ,  [   7.0  ,   200  ]    -->     6.1
[   7.9  ,   500  ]  ,  [   7.0  ,   600  ]    -->     2.5
[   7.9  ,   100  ]  ,  [   7.0  ,   600  ]    -->     6.8

"""


def solve(before, after):
    before_litres = before[0] * before[1]
    after_litres = after[0] * after[1]
    litres_used = after_litres - before_litres
    distance = after[1] - before[1]
    return round(litres_used / distance, 1)


result = solve([7.9, 100], [7.0, 200])
print(result)
