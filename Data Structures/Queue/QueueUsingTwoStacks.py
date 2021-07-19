class Stack:
    def __init__(self):
        self.items = []
    def push(self, x):
        self.items.append(x)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, x):
        self.stack1.push(x)

    def dequeue(self):
        if not self.stack2.items:
            while self.stack1.items:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.pop()
    
    def print(self):
        if not self.stack2.items:
            while self.stack1.items:
                self.stack2.push(self.stack1.pop())
        
        return self.stack2.peek()


if __name__ == "__main__":
    myQueue = Queue()
    for q in range(int(input())):
        query = input().split()
        if query[0] == "1":
           myQueue.enqueue(int(query[1]))
        if query[0] == "2":
            myQueue.dequeue()
        if query[0] == "3":
            print(myQueue.print())