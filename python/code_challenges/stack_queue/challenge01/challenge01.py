# Write here the code challenge solution


'''Create class for the queue'''
class MyQueue:

    def __init__(self):
        '''defined a two stack'''
        self.front = []
        self.rear = []

    # Here create push function
    def push(self, item):
        '''Push a new node in a stack'''
        while self.front:
            self.rear.append(self.front.pop())
            
        self.front.append(item)
        while self.rear:
            self.front.append(self.rear.pop())

    # Here create pop function
    def pop(self):
        '''remove an item from the queue'''
        if len(self.front) == 0:
            print("Queue is empty")
        else:
            return self.front.pop()

    # Here create peek function 
    def peek(self):
        '''get the peek item from stack'''
        return self.front[-1]

    # Here create empty function 
    def empty(self):
        '''check if the stack empty or not'''
        return not self.front
        

queue = MyQueue()
queue.push(1)
queue.push(2)
print("Number pop is       -->", queue.pop())
print("The peek number is --> ", queue.peek())


# queue = queue()
# for i in range(5):
#     queue.push(i)

# for i in range(5):
#     print(queue.pop())