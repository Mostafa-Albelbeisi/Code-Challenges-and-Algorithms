# Write here the code challenge solution

class Node:
    """This class creates the node """
    def __init__(self, value):
        self.data = value
        self.next = None

class linkedList:
    """this class append and delete a node"""
    def __init__(self):
        self.head = None

	
    def append(self, value):
        """this is responseble to append a node"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def deleteNTHNode(self, n):
        "This is Remove nth Node function"
        first = self.head
        last = self.head
        for i in range(n):
            if(first.next == None):
                if(i == n - 1):
                    self.head = self.head.next
                return self.head
            first = first.next
        while(first.next != None):
            first = first.next
            last = last.next
        last.next = last.next.next
	
    def printAll(self):
        """this is for printing"""
        list=[]
        current = self.head
        while(current != None):
            print(current.data)
            list.append(current.data)
            current = current.next
        return list

linkedList1 = linkedList()
linkedList1.append(5)
linkedList1.append(4)
linkedList1.append(3)
linkedList1.append(2)
linkedList1.append(1)
print("Created Linked list --> ")
linkedList1.printAll()
linkedList1.deleteNTHNode(2)
print("Linked List after delete --> ")
linkedList1.printAll()


linkedList2 = linkedList()
linkedList2.append(2)
linkedList2.append(1)
print("Created Linked list --> ")
linkedList2.printAll()
linkedList2.deleteNTHNode(1)
print("Linked List after delete --> ")
linkedList2.printAll()