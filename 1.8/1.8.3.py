n=int(input())
y=0
for i in range(1,n+1):
    x=str(input())
    if "rat" in x:
        y=i
        print(y)
if y==0:
    y=-1
    print(y)
