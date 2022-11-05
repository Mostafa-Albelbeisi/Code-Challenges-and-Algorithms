# Write here the code challenge solution

class Node:
    def __init__(self, item):
        self.next = None
        self.item = item

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        '''pushes a new node to the top of the stack'''
        node = Node(item)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        '''remove an item from the top'''
        if self.top:
            temp = self.top
            self.top = self.top.next
            self.size -= 1
            return temp.item
        else:
            return("Stack is empty")
    
    def peek(self):
        '''get the peek item from stack, return the vlaue located on top'''
        if self.top:
            return self.top.item
        else:
            return("Stack is empty")

    def empty(self):
        '''Check if the stack empty or not'''
        return self.size == 0
    
    def get_size(self):
        return self.size

def validParentheses(s):
    '''Here this function check if it is a valid parentheses or not'''
    Parentheses={'(':')', '{':'}', '[':']'}
    stack=Stack()
    for i in s:
        if i in Parentheses.keys():
            stack.push(i)
        elif i in Parentheses.values():
            if stack.empty():
                return False
            if Parentheses[stack.pop()] != i:
                return False
    return stack.empty()
