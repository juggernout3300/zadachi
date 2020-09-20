n=int(input())
x=0
if n==2 or n==3 or n==5:
    print("Простое")
else:
    for i in range(2, n):
        if (n%i)==0:
            x=2
            break
    if x==0:
        print("Простое")
    elif x==2:
        print("Составное")