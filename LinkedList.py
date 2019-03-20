class LinkedList:

    # class for a node
    class ListNode:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_begin(self, value):
        node = self.ListNode(value)
        node.next = self.head
        self.head = node

        if self.tail is None:
            self.tail = node

        return node

    def insert_at_end(self, value):
        node = self.ListNode(value)
        node.next = None
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node
        return node

    def insert_list(self, items: list):
        for x in items:
            self.insert_at_end(x)

    def deque(self):
        if self.head is None:
            return None
        node = self.head
        self.head = node.next
        if self.head is None:
            self.tail = None
        return node.value    # value is asssumed to be not null

    def print_list(self):
        next_node = self.head
        while next_node is not None:
            print(next_node.value)
            next_node = next_node.next
        print('---------')

    def length(self):
        list_len = 0
        next_item = self.head
        while next_item is not None:
            list_len += 1
            next_item = next_item.next

        return list_len

    def test_1(self):
        self.__init__()
        self.print_list()
        self.insert_at_end(99)
        self.print_list()
        self.insert_at_begin('a')
        self.print_list()
        self.insert_at_begin('b')
        self.print_list()
        self.insert_at_end(98)
        self.print_list()
        print(self.length())

    def test_2(self):
        self.__init__()
        self.insert_at_end(99)
        self.insert_at_begin('a')
        self.insert_at_begin('b')
        self.insert_at_end(98)

        v = self.deque()
        while v is not None:
            print(v, end=", ")
            v = self.deque()
        print('')

    def test_3(self):
        d = dict()
        d['v'] = 10
        d['l'] = None
        d['r'] = None
        self.__init__()
        self.insert_at_end(d)
        self.print_list()

    def get_kth_from_end(self, k: int):
        n: self.ListNode = self.head

        # first skip k items and set a trailing pointer
        for _ in range(k):
            if n is None:
                return None
            n = n.next

        trailing_ptr: self.ListNode = self.head
        while n is not None:
            n = n.next
            trailing_ptr = trailing_ptr.next

        # trailing_ptr might be None if k passed is 0
        if trailing_ptr is not None:
            return trailing_ptr.value

        return None

