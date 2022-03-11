# He first turns and travels 10 units of distance
#  His second turn is upward for 20 units
#  Third turn is to the left for 30 units
#  Fourth turn is the downward for 40 units
#  Fifth turn is to the right(again) for 50 units
# … And thus he travels, every time increasing the travel distance by 10 units.

# Input: 3

# Output: -20 20
# ------------------------------------------------------------------------------
def fun():
    inp = int(input())
    x ,y = 0, 0
    distance = 10
    for i in range(inp):
        if i%4 == 0: x += distance
        elif i%4 == 1: y += distance
        elif i%4 == 2: x -= distance
        else: y -= distance
        distance += 10
    print(x,y,sep=" ")
fun()