queue = list()
#two main method are 
# append or insert
# pop[0] 
# to check top [-1]
def enqueue():
    element = input("enter the element")
    queue.append(element)
    #print(queue)
def dequeue():
    if not queue:
        print("queue is empty")
    else:
        e = queue.pop(0)
        print("removed elemtn is ",e)
        #print(queue)
def top():
    print(queue[-1])
def printing():
    print(queue)
while True:
    print("select the operation \n 1.enqueue 2.dequeue 3.viewtop 4.print 5.quit" )
    choice = int(input())
    if choice ==1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        top()
    elif choice == 4:
        printing()
    elif choice == 5:
        break
    else:
        print('enter the correct operation')
