class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_tree_balanced(node: BinaryTree) -> bool:
    
    def check_height(node: BinaryTree) -> int:
        if node is None:
            return 0
        
        left_height = check_height(node.left)
        if left_height == -1:
            return -1
        
        right_height = check_height(node.right)
        if right_height == -1:
            return -1
        
        if abs(left_height - right_height) > 1:
            return -1
        
        return max(left_height, right_height) + 1
    
    return check_height(node) != -1

root1 = BinaryTree(1)
root1.left = BinaryTree(2)
root1.right = BinaryTree(3)
root1.left.left = BinaryTree(4)
root1.left.right = BinaryTree(5)

print(is_tree_balanced(root1))
root2 = BinaryTree(1)
root2.left = BinaryTree(2)
root2.left.left = BinaryTree(3)

print(is_tree_balanced(root2))

print(is_tree_balanced(None))

root4 = BinaryTree(1)
print(is_tree_balanced(root4))

root5 = BinaryTree(1)
root5.left = BinaryTree(2)
root5.right = BinaryTree(3)
root5.left.left = BinaryTree(4)
root5.left.left.left = BinaryTree(5)

print(is_tree_balanced(root5))
