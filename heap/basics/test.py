"""
Run heapify on [9, 5, 6, 2, 3]. Start at index n//2 - 1 and sift down to index 0.
Put up as a heap -> then make it a valid min/max heap in place
Answer:
idx 0: children 2 and 6, the smaller is 2, swap → [2, 9, 6, 5, 3]
idx 1: 9 has children 5 and 3, the smaller is 3, swap → [2, 3, 6, 5, 9]
idx 4: no children, stop.

Final heap: [2, 3, 6, 5, 9]

        2
      /   \
     3     6
    / \
   5   9

"""

"""
Sort a list using only a heap

import heapq

def heap_sort(nums):
    heap = []
    # 1. put every number into the heap
    for n in nums:
        heapq.heappush(heap, n)
    # heapq.heapify(heap)

    result = []
    # 2. pop until the heap is empty, appending each popped value to result
    while heap:
        result.append(heapq.heappop(heap))

    return result


if __name__ == "__main__":
    print(heap_sort([5, 3, 8, 1, 4]))   # expected: [1, 3, 4, 5, 8]
    print(heap_sort([]))                # expected: []
    print(heap_sort([2, 2, 1]))         # expected: [1, 2, 2]
"""

"""
Return the 3 smallest elements

import heapq

def three_smallest_manual(nums):
    heap = nums[:]            # copy so we don't change the caller's list
    # 1. turn it into a heap
    heapq.heapify(heap)

    result = []
    count = 0
    # 2. pop 3 times, but be careful: what if nums has fewer than 3 elements?
    while heap:

        if count == 3:
            break
        result.append(heapq.heappop(heap))
        count += 1

    return result
        

def three_smallest_builtin(nums):
    # use heapq.nsmallest(n, iterable)
    heap = nums[:]
    heapq.heapify(heap)

    return heapq.nsmallest(3, heap)


if __name__ == "__main__":
    print(three_smallest_manual([7, 2, 9, 1, 5, 3]))    # expected: [1, 2, 3]
    print(three_smallest_builtin([7, 2, 9, 1, 5, 3]))   # expected: [1, 2, 3]
    print(three_smallest_manual([4, 1]))                # expected: [1, 4]
    print(three_smallest_builtin([4, 1]))               # expected: [1, 4]
"""

"""
Build a max-heap with negation
"""
import heapq

def descending_order(nums):
    heap = [-n for n in nums]     # right: [-4, -1, -7, -3]
    # 1. push each number into the heap (what do you push?)
    heapq.heapify(heap)
    result = []
    # 2. pop until empty (what do you append to result?)
    while heap:
        result.append(-(heapq.heappop(heap)))

    return result


if __name__ == "__main__":
    print(descending_order([4, 1, 7, 3]))   # expected: [7, 4, 3, 1]
    print(descending_order([]))             # expected: []
    print(descending_order([5, 5, 2]))      # expected: [5, 5, 2]