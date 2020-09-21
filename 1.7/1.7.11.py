n=int(input())
x="коров"
y="корова"
z="коровы"
for i in range (1, n+1):
    s=i%10
    if s==1 and i!=11:
        j=y
        print("На лугу", i, j)
    elif 1<s<5 and i!=11 and i!=12 and i!=13 and i!=14:
        j=z
        print("На лугу", i, j)
    else:
        j=x
        print("На лугу", i, j)


