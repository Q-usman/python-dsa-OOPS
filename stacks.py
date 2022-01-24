stack = list()
#two main method are 
# append
#pop
# to check top [-1]

def push():
    element = input("enter the element")
    stack.append(element)
    #print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        e = stack.pop()
        print("removed elemtn is ",e)
        #print(stack)
def top():
    print(stack[-1])
while True:
    print("select the operation \n 1.push 2.pop 3.Quit")
    choice = int(input())
    if choice ==1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        break
    else:
        print('enter the correct operation')
