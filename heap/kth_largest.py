"""
Kth Largest Element in a Stream
Easy
Topics
Company Tags
Hints
Design a class to find the kth largest integer in a stream of values, including duplicates. E.g. the 2nd largest from [1, 2, 3, 3] is 3. The stream is not necessarily sorted.

Implement the following methods:

constructor(int k, int[] nums) Initializes the object given an integer k and the stream of integers nums.
int add(int val) Adds the integer val to the stream and returns the kth largest integer in the stream.
Example 1:

Input:
["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

Output:
[null, 3, 3, 3, 5, 6]

Explanation:
KthLargest kthLargest = new KthLargest(3, [1, 2, 3, 3]);
kthLargest.add(3);   // return 3
kthLargest.add(5;   // return 3
kthLargest.add(6);   // return 3
kthLargest.add(7);   // return 5
kthLargest.add(8);   // return 6

Constraints:
1 <= k <= 1000
0 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-1000 <= val <= 1000
There will always be at least k integers in the stream when you search for the kth integer.

"""

import heapq
import random
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums[:]          # copy so we don't mutate the caller's list
        heapq.heapify(self.heap)     # O(n)
        # Trim down to the k largest elements
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)  # pop smallest + push val in one step
        return self.heap[0]


def run_operations(ops, args):
    """Mimic the LeetCode-style input: method names and their arguments."""
    obj = None
    results = []
    for op, arg in zip(ops, args):
        if op == "KthLargest":
            obj = KthLargest(arg[0], arg[1])
            results.append(None)
        elif op == "add":
            results.append(obj.add(arg[0]))
    return results


if __name__ == "__main__":
    # Example 1 from the problem
    ops = ["KthLargest", "add", "add", "add", "add", "add"]
    args = [[3, [1, 2, 3, 3]], [3], [5], [6], [7], [8]]
    output = run_operations(ops, args)
    print("Output:", output)
    assert output == [None, 3, 3, 3, 5, 6]

    # Edge case: start empty, k = 3 (only check once the stream has >= k items)
    kl = KthLargest(3, [])
    assert [kl.add(x) for x in [4, 5, 8, 2]][2:] == [4, 4]

    # Randomized check against sorting
    for _ in range(200):
        k = random.randint(1, 10)
        nums = [random.randint(-100, 100) for _ in range(random.randint(0, 20))]
        kl = KthLargest(k, nums)
        data = nums[:]
        for _ in range(30):
            v = random.randint(-100, 100)
            data.append(v)
            result = kl.add(v)
            if len(data) >= k:  # the kth largest only exists with >= k elements
                assert result == sorted(data, reverse=True)[k - 1]

    print("All tests passed!")