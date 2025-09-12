heap = [0 for _ in range(10001)]  # allocate enough space
curr_size = 0

# Function to maintain heap property moving up
def heapify_up(i):
    while i > 0 and heap[(i - 1) // 2] > heap[i]:
        heap[(i - 1) // 2], heap[i] = heap[i], heap[(i - 1) // 2]
        i = (i - 1) // 2

# Function to maintain heap property moving down
def heapify_down(i):
    global curr_size
    while True:
        l = 2 * i + 1
        r = 2 * i + 2
        smallest = i

        if l < curr_size and heap[l] < heap[smallest]:
            smallest = l
        if r < curr_size and heap[r] < heap[smallest]:
            smallest = r

        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            i = smallest
        else:
            break

# Function to insert a value in Heap.
def insertKey(x):
    global curr_size
    heap[curr_size] = x
    heapify_up(curr_size)
    curr_size += 1

# Function to delete a key at ith index.
def deleteKey(i):
    global curr_size
    if i >= curr_size:
        return
    heap[i] = float('-inf')
    heapify_up(i)
    extractMin()  # remove it

# Function to extract minimum value in heap
def extractMin():
    global curr_size
    if curr_size <= 0:
        return -1
    root = heap[0]
    heap[0] = heap[curr_size - 1]
    curr_size -= 1
    heapify_down(0)
    return root
# Example 1
curr_size = 0
insertKey(4)
insertKey(2)
print(extractMin())  # 2
insertKey(6)
deleteKey(0)
print(extractMin())  # 6
print(extractMin())  # -1

# Example 2
curr_size = 0
insertKey(8)
insertKey(9)
deleteKey(1)
print(extractMin())  # 8
print(extractMin())  # -1
