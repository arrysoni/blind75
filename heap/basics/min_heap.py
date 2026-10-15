"""
Min Heap From Scratch

A min heap is a complete binary tree stored in an array, where every parent is ≤ its children. It only guarantees the top element is the smallest. It does not keep everything sorted.

Array layout (0-indexed), for node at index i:
parent: (i - 1) // 2
left child: 2*i + 1
right child: 2*i + 2
"""

class MinHeap:

    def __init__(self):
        self.h = []

    def push(self, val):  # O(log n)
        self.h.append(val)
        self._sift_up(len(self.h) - 1)

    def pop(self): # O(log n)
        if not self.h:
            raise IndexError("empty heap")

        top = self.h[0]
        last = self.h.pop()

        if self.h:
            self.h[0] = last
            self._sift_down(0)
        return top

    def peek(self): # O(1)
        return self.h[0]

    def _sift_up(self, i):

        while i > 0:
            p = (i-2) // 2
            if self.h[p] <= self.h[i]:
                break
            self.h[p], self.h[i] = self.h[i], self.h[p]
            i = p

    def _sift_down(self, i):
        n = len(self.h)  # current heap size, used to check if a child exists

        while True:
            smallest = i                    # assume current node is the smallest
            l, r = 2*i + 1, 2*i + 2         # left and right child indices

            # if left child exists and is smaller, it becomes the candidate
            if l < n and self.h[l] < self.h[smallest]:
                smallest = l

            # if right child exists and is smaller than the best so far, it wins
            if r < n and self.h[r] < self.h[smallest]:
                smallest = r

            # heap property holds here: neither child is smaller, so we're done
            if smallest == i:
                break

            # otherwise swap with the smaller child and keep sinking
            self.h[i], self.h[smallest] = self.h[smallest], self.h[i]
            i = smallest

            
if __name__ == "__main__":
    heap = MinHeap()
    for x in [5, 3, 8, 1, 4]:
        heap.push(x)
        print(f"pushed {x}: {heap.h}")

    print("peek:", heap.peek())

    while heap.h:
        print("popped:", heap.pop(), "->", heap.h)
