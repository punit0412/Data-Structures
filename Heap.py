capacity = 10

class Heap:

    def __init__(self):
        # this is actual number of items in heap
        self.heap_size = 0
        # this is underlying data structure
        self.heap = [0]*capacity

    def insert(self,item):
        if self.heap_size == capacity:
            return

        self.heap[self.heap_size] = item
        self.heap_size += 1

        # check the heap properties

        self.fix_up(self.heap_size-1)
    # starting with the actual node we have inserted up to root node
    # we have to compare the values whether to make swap operations
    # logN it has O(logN) running time complexity


    def fix_up(self,index):

        parent_index = (index-1)//2

        # we consider all the items above till we hit the root node
        # if heap property is violated than we swap the parent-child

        if index > 0 and (self.heap[index] > self.heap[parent_index]):
            self.heap[index],self.heap[parent_index] = self.heap[parent_index],self.heap[index]
            self.fix_up(parent_index)

    def get_max(self):
        return self.heap[0]

    # return max and removes it as well
    # remove the root node of the heap

    def poll(self):
        max_item = self.get_max()

        # swap the root with the last item and "heapify"
        self.heap[0],self.heap[self.heap_size-1] = self.heap[self.heap_size-1],self.heap[0]
        self.heap_size -= 1
        # make sure the heap is "heapify"

        self.fix_down(0)
        return max_item
    # starting with the root node downwards until the heap properties are no longer violated
    def fix_down(self,index):
        left_index = 2*index + 1
        right_index = 2*index+2

        largest_index = index

        # looking for the largest (parent or left node)
        if left_index < self.heap_size and self.heap[left_index] > self.heap[largest_index]:
            largest_index = left_index

        # if the right child is greater tha the left child : largest is the right child
        if right_index < self.heap_size and self.heap[right_index] > self.heap[largest_index]:
            largest_index = right_index

        # if the parent is larger than the children : it is a valid heap so we terminate the recursive function calls
        if index != largest_index:
            self.heap[index],self.heap[largest_index] = self.heap[largest_index],self.heap[index]
            self.fix_down(largest_index)


    def heap_sort(self):
        arr = []
        for  _ in range(self.heap_size):
            max_num = self.poll()
            arr.append(max_num)
        return arr


heap = Heap()
heap.insert(5)
heap.insert(2)
heap.insert(6)
heap.insert(8)
heap.insert(9)
heap.insert(-1)
heap.insert(3)
print(heap.heap_sort())






