from LinkedList import LinkedList


class BinaryTree:
    
    class TreeNode:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
            
    def __init__(self):
        self.root: self.TreeNode = None

    def add_root_node(self, value):
        if self.root is not None:
            print("::::::! Tree exists - overwriting it! :::::::::")
        node = self.TreeNode(value)
        node.left = None
        node.right = None
        self.root = node
        return node

    def add_left_node(self, root_node, value):
        if root_node is None:
            raise ValueError("root node passed is null")

        node = self.TreeNode(value)
        node.left = None
        node.right = None
        root_node.left = node
        return node

    def add_left_subtree(self, subtree):
        if self.root is None:
            raise ValueError("root node of tree is null")
        if not isinstance(subtree, self.TreeNode):
            raise ValueError("subtree passed to add_left_subtree is not of type TreeNode")
        self.root.left = subtree

    def add_right_subtree(self, subtree):
        if self.root is None:
            raise ValueError("root node of tree is null")
        if not isinstance(subtree, self.TreeNode):
            raise ValueError("subtree passed to add_right_subtree is not of type TreeNode")
        self.root.right = subtree

    def add_right_node(self, root_node, value):
        if root_node is None:
            raise ValueError("root node passed is null")

        node = self.TreeNode(value)
        node.left = None
        node.right = None
        root_node.right = node
        return node

    def inorder(self, node):
        # left, root, right
        if node is not None:
            self.inorder(node.left)
            print(node.value, end=' ')
            self.inorder(node.right)

    def preorder(self, node):
        # root, left, right
        if node is not None:
            print(node.value, end=' ')
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        # left, right, root
        if node is not None:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value, end=' ')

    def breadth_first(self):
        if self.root is None:
            return
        ls = LinkedList()
        ls.insert_at_begin(self.root)
        item_from_queue = ls.deque()
        while item_from_queue is not None:
            value = item_from_queue.value
            left_node = item_from_queue.left
            right_node = item_from_queue.right
            print(value, end=", ")
            if left_node is not None:
                ls.insert_at_end(left_node)
            if right_node is not None:
                ls.insert_at_end(right_node)
            # deque next
            item_from_queue = ls.deque()

        print('')

    def test_1(self):
        self.__init__()
        n1 = self.add_root_node(1)
        n2 = self.add_left_node(n1, 2)
        n3 = self.add_right_node(n1, 3)
        n4 = self.add_left_node(n2, 4)
        n5 = self.add_right_node(n2, 5)
        n6 = self.add_right_node(n3, 6)
        n7 = self.add_right_node(n5, 7)
        n8 = self.add_left_node(n6, 8)

        self.inorder(self.root)
        print('')
        self.preorder(self.root)
        print('')
        self.postorder(self.root)
        print('')

        # another example
        self.__init__()
        n25 = self.add_root_node(25)
        n15 = self.add_left_node(n25, 15)
        n10 = self.add_left_node(n15, 10)
        n4 = self.add_left_node(n10, 4)
        n12 = self.add_right_node(n10, 12)
        n22 = self.add_right_node(n15, 22)
        n18 = self.add_left_node(n22, 18)
        n24 = self.add_right_node(n22, 24)
        n50 = self.add_right_node(n25, 50)
        n35 = self.add_left_node(n50, 35)
        n31 = self.add_left_node(n35, 31)
        n44 = self.add_right_node(n35, 44)
        n70 = self.add_right_node(n50, 70)
        n66 = self.add_left_node(n70,66)
        n90 = self.add_right_node(n70, 90)

        self.inorder(self.root)
        print('')
        self.preorder(self.root)
        print('')
        self.postorder(self.root)
        print('')

    def test_2(self):
        self.__init__()
        n1 = self.add_root_node(1)
        n2 = self.add_left_node(n1, 2)
        n3 = self.add_right_node(n1, 3)
        n4 = self.add_left_node(n2, 4)
        n5 = self.add_left_node(n3, 5)
        n6 = self.add_right_node(n3, 6)
        n7 = self.add_left_node(n4, 7)
        n8 = self.add_right_node(n4, 8)
        n9 = self.add_right_node(n5, 9)
        n10 = self.add_left_node(n6, 10)
        n11 = self.add_right_node(n6, 11)

        self.inorder(self.root)
        print('')
        self.preorder(self.root)
        print('')
        self.postorder(self.root)
        print('')
        print('---------------------------')
        self.breadth_first()

    def test_3(self, in_list: list, pre_list: list, post_list: list) -> bool:
        # check if the three lists are for the same binary tree
        if not (len(in_list) == len(pre_list) == len(post_list)):
            return False

        # construct the tree from the in_list and pre_list

