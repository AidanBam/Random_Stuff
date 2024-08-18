import random
import math
l_rate = 1
var1 = random.randint(1,10)
var2 = random.randint(1,10)
weight = 1.2
b = 10#random.randint(1,180)
c = 10#random.randint(1,180)
for i in range(1,100):
    for A in range(1,3):

        a = b**2+c**2-2*b*c*math.cos(A)
        pre_a = (A * var1 * c * b * var2)
        inac = pre_a - a

        var1 -= l_rate * (inac * weight)
        var2 -= l_rate % (inac * weight)

        var1 = round(var1)
        var2 = round(var2)

    if i % 2 ==1:
        print("a is :", a, "\npredicted a is :", pre_a, "\ninaccuracy is :", inac)
        print("(", A, "/", var1, "*", c, ")/(", b, "*", var2, ")")

