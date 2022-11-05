class Node:
    def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def preorder(self):
        """returns array of values ordered root, left, right"""
        output = []
        def pre_order(root):
            if not root:
                return 'Sorry the tree its empty'

            output.append(root.value)
            pre_order(root.left)
            pre_order(root.right)

        pre_order(self.root)
        return output

    def inorder(self):
        """returns array of values ordered left, root, right"""
        output = []
        def in_order(root):
            if not root:
                return
            in_order(root.left) # check left
            output.append(root.value) # root
            in_order(root.right) # check right
        in_order(self.root)
        return output


    def traversal(self): 
        '''
        doing a breadth first traversal of the tree, and print the values of the nodes of the tree in the breadth first order
        '''
        if not self.root :
            return "Sorry the tree its empty"
        output = []
        Queue = []    
        Queue = Queue + [self.root]

        while Queue : 
            current = Queue[0]
            if current.left: 
                Queue += [current.left]
            if current.right: 
                Queue += [current.right]
            output = output+[Queue.pop(0).value]
        return output 


tree=BinaryTree()
tree.root = Node(3)
tree.root.left = Node(9)
tree.root.right = Node(20)
tree.root.right.left = Node(15)
tree.root.right.right = Node(7)
print("Preorder  --> " ,tree.preorder())
print("Inorder   --> " ,tree.inorder())
print("Traversal --> " ,tree.traversal())