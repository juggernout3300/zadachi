a=int(input())
b=int(input())
if b > a:
    j = 0
    for i in range(a, b):
        j += (i**2)
    print(j)
elif a > b:
    x = 0
    for i in range(b, a):
        x += (i**2)
    print(x)

