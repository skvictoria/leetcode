import sys

input = sys.stdin.readline
values = [int(input()) for _ in range(3)]
a,b,c = values
if ((a+b+c) != 180):
    print("Error")
else:
    if a==b and b==c:
        print("Equilateral")
    elif a==b or b==c or c==a:
        print("Isosceles")
    else:
        print("Scalene")