class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)


def maxDepth(root):
    if root is None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


print(maxDepth(root))
