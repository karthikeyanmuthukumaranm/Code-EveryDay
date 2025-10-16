class Queue:
    def __init__(self):
        self.queue=[]
    def enqueue(self,item):
        self.queue.append(item)
        print(f"{item} added")
    def dequeue(self):
        if not self.is_empty():
            remove=self.queue.pop()
            print(f"{remove} is poped")
        else:
            print("queue empty")
    def peek(self):
        if not self.is_empty():
            print(f"last elemented is {self.queue[0]}")
        else:
            print("empty nothing")
    def is_empty(self):
        return len(self.queue)==0
        
    def display(self):
        print(f"current queue is :{self.queue}")
queue=Queue()

while True:
    choice =input("enter number 1 - 5")
    if choice=='1':
        value=int(input("enter number:"))
        queue.enqueue(value)

    elif choice =='2':
        queue.dequeue()
    elif choice =='3':
        queue.peek()
    elif choice =='4':
        queue.display()
    elif choice == '5':
        print("exiting")
        break
    else:
        print("enter valid number")
                
