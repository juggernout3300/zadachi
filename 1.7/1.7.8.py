num1 = int(input())
n1,n2 = 1,1
count = 0
result = []

if num1 == 0:
    print()
elif num1 == 1:
    print(n1)
else:
    while count < num1:
        result.append(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count +=1
list = ' '.join(str(elem) for elem in result)
print(list)
