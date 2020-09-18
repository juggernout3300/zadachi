z=int(input())
n=int(input())
k=0
for i in range(0,n):
    j=int(input())
    k+=j
if k<=z:
    print("Покупает")
elif k>z:
    print("Не покупает")
