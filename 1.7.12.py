n=int(input())
a = 1
b = 1
if n==0:
    print()
elif n==1:
    print(1)
elif n>1:
        print(1, end=" ")
        print(1, end=" ")
        for i in range(1, n-1):
            s=a+b
            a=b
            b=s
            print(s, end=" ")
