
class heap:
    @staticmethod
    def heapify(a: list, type_min: bool) -> list:

        result = [0] * len(a)
        insertion_inx = 0

        for x in a:

            # first insert the item at the end of the list
            result[insertion_inx] = x

            # Now bubble up the inserted item if not the root
            current_inx = insertion_inx

            while True:
                if current_inx == 0:
                    break
                # compute parent. If i is even parent = (i div 2) - 1 else (i div 2)
                if current_inx % 2 == 0:
                    parent_inx = (current_inx // 2) - 1
                else:
                    parent_inx = current_inx // 2

                # swap item and parent if needed (parent > item in min heap or parent < item in max heap)
                if (type_min and result[parent_inx] > x) or (not type_min and result[parent_inx] < x):
                    result[parent_inx], result[current_inx] = result[current_inx], result[parent_inx]
                    current_inx = parent_inx
                else:
                    break

            # increment the insertion index
            insertion_inx += 1

        return result

    def heap_sort(self, ascending: bool) -> list:

        orig_len = len(a)
        result = [0] * orig_len
        curr_len = orig_len
        curr_list = a[0:curr_len]

        while curr_len > 0:
            # heapify the tree
            heap = heapify(curr_list, ascending)

            # now root has the min or max
            result[orig_len - curr_len] = heap[0]

            # replace first by last item of heap and reduce lebgth by 1
            heap[0] = heap[-1]
            curr_len -= 1
            curr_list = heap[0:curr_len]

        return result

    def __init__(self, a: list, type_min: bool):
        self.type_min = type_min
        self.heap_length = len(a)
        self.heap = self.heapify(a, type_min)

    def pop(self):
        curr_len = self.heap_length
        if curr_len == 0:
            return None

        top_item = self.heap[0]
        if curr_len == 1:
            self.heap_length = 0
            return top_item

        # replace top by last
        self.heap[0] = self.heap[curr_len - 1]
        self.heap = self.heapify(self.heap[0:curr_len - 1], self.type_min)
        self.heap_length = curr_len - 1

        return top_item

    def insert(self, item):
        curr_len = self.heap_length
        if curr_len == 0:
            self.__init__([item], self.type_min)
        else:
            self.heap.append(item)
            self.heap = self.heapify(self.heap[0:curr_len + 1], self.type_min)
            self.heap_length = curr_len + 1




