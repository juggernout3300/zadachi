n=int(input())
x=range(1,n+1)
for j in x:
    for i in x:
        print(j*i, end="\t")
    print(end="\n")