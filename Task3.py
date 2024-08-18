import math
print("Question 1")
q = int(1)
while q == 1:
    num = int(input("\nEnter a number: "))
    if num >= 10000:
        print("\nBreak your own computer\n")
    else:
        nu = 1
        while nu <= num:
            print(nu)
            nu = int(nu + 1)
            q = 2

print("Question 2")

r = float(input("Radius: "))
d = r * 2
ReAr = math.pi * r**2
EqAr = (64/81) * d**2
print("Eqyption Area = " + str(EqAr))
print("Real Area = " + str(ReAr))

print("Question 3")

ttl = int(input("Time to launch: "))
print("Counting down ...")
while ttl > 0:
    print(str(ttl) + " ...")
    ttl=ttl-1
print("Lift Off!")


