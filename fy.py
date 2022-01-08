n = int(input())
numbers = []
for i in range(0,n-1):
    x = int(input('enter the number: '))
    numbers.append(x)
numbers.sort()
print(numbers)
mx = max(numbers)
print(mx)
for i in range(mx):
    if i in numbers:
        continue
    else:
        print(i)
