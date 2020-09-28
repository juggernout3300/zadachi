a=int(input())
x=0
while x==0:
    for i in range(2, a+1):
        b=a/i
        c=a%i
        if c == 0:
            x = 1
            print(i)
            break
        elif c == 0 and i == a:
            x = 1
            print(i)
            break