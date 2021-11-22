class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 # by number of nodes

'''
assumptions

arr is sorted with unique elements

returns root node
'''

class AVL_Tree():

    def __init__(self):
        self.root = None

    # O(log n)
    def insert(self, root, value):
        # regular bst insertion
        if root is None:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # update height
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # balance
        balance = self.get_balance(root)

        # determine rotation
        # tree is assumed balanced after each insert
        #
        # left subtree became imbalanced
        if balance > 1 and value < root.left.value:
            return self.rotate_right(root)

        # right subtree became imbalanced
        if balance < -1 and value > root.right.value:
            return self.rotate_left(root)

        # left subtree became imbalanced
        # rotate left subtree to the left first because node with value is in the right subtree of root.left
        if balance > 1 and value > root.left.value:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # right subtree became imbalanced
        # rotate right subtree to the right first because node with value is in the left subtree of root.right
        if balance < -1 and value < root.right.value:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # O(1)
    def rotate_left(self, node):
        right = node.right  # new root
        right_child_left = right.left

        # rotate
        right.left = node   # current root becomes left child of new root
        node.right = right_child_left   # left child of new root becomes right child of current root

        # update heights
        # O(1)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        right.height = 1 + max(self.get_height(right.left), self.get_height(right.right))

        # right is the new root
        return right

    # O(1)
    def rotate_right(self, node):
        left = node.left    # new root
        left_child_right = left.right

        # rotate
        left.right = node   # current root becomes right child of new root
        node.left = left_child_right    # right child of new root becomes left child of current root

        # update heights
        # O(1)
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))
        left.height = 1 + max(self.get_height(left.left), self.get_height(left.right))

        # left is the new root
        return left

    # O(1)
    def get_height(self, root):
        return 0 if root is None else root.height


    # O(1)
    def get_balance(self, root):
        return 0 if root is None else self.get_height(root.left) - self.get_height(root.right)

    def traverse_preorder(self, root):
        if root is None:
            return

        print(f'{root.value}')
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)
    

    def build(self, arr):
        for value in arr:
            self.root = self.insert(self.root, value)

        return self.root

if __name__ == "__main__":
    case1 = [1,2,4,5,6,7,8,9]
    tree1 = AVL_Tree()
    root1 = tree1.build(case1)
    tree1.traverse_preorder(root1)
    print(f'height: {root1.height}')
