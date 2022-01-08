n = int(input('enter the size'))
li = []
for i in range(0,n-1):
    x = int(input('enter the number'))
    li.append(x)
Li = set(li)
for i in range(n):
    if i in Li:
        continue
    else:
        print(i)

