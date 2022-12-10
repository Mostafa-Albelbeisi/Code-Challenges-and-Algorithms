# Write here the code challenge solution
class Tree:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def Target(root, k):
    """
    function that takes a Binary Search tree and an integer as a parameter. Return True if Binary search tree has two elements that their summation is the given integer.
    """
    values = []

    def twoSumBST(node):
        if not node:
            return False
        x = k - node.val
        if x in values:
            return True
        else:
            values.append(node.val)
        return twoSumBST(node.left) or twoSumBST(node.right)

    return twoSumBST(root)
