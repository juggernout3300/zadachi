n = int(input())
x = 0
while x<n:
    y = int(input())
    x += y
    if x>n:
        x-=y
        break
print("Стоп, Джон!")
print(x)