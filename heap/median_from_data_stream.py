"""
The median is the middle value in a sorted list of integers. For lists of even length, there is no middle value, so the median is the mean of the two middle values.

For example:

For arr = [1,2,3], the median is 2.
For arr = [1,2], the median is (1 + 2) / 2 = 1.5

Implement the MedianFinder class:
MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far.

Example 1:
Input:
["MedianFinder", "addNum", "1", "findMedian", "addNum", "3" "findMedian", "addNum", "2", "findMedian"]
Output:
[null, null, 1.0, null, 2.0, null, 2.0]

Explanation:
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.findMedian(); // return 1.0
medianFinder.addNum(3);    // arr = [1, 3]
medianFinder.findMedian(); // return 2.0
medianFinder.addNum(2);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0

Constraints:
-100,000 <= num <= 100,000
At most 50,000 calls will be made to addNum and findMedian.
findMedian will only be called after adding at least one integer to the data structure.

"""
import heapq
import random
import statistics


class MedianFinder:

    def __init__(self):
        self.small = []  # max-heap (store negatives)
        self.large = []  # min-heap

    def addNum(self, num: int) -> None:
        # Push into small, then move small's max into large
        heapq.heappush(self.small, -num)
        heapq.heappush(self.large, -heapq.heappop(self.small))

        # Rebalance so small has >= as many elements as large
        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        return (-self.small[0] + self.large[0]) / 2.0


def run_operations(ops, args):
    """Mimic the LeetCode-style input: a list of method names and their arguments."""
    mf = None
    results = []
    for op, arg in zip(ops, args):
        if op == "MedianFinder":
            mf = MedianFinder()
            results.append(None)
        elif op == "addNum":
            mf.addNum(arg[0])
            results.append(None)
        elif op == "findMedian":
            results.append(mf.findMedian())
    return results


if __name__ == "__main__":
    # Example 1 from the problem
    ops = ["MedianFinder", "addNum", "findMedian", "addNum", "findMedian", "addNum", "findMedian"]
    args = [[], [1], [], [3], [], [2], []]
    output = run_operations(ops, args)
    print("Output:", output)
    assert output == [None, None, 1.0, None, 2.0, None, 2.0]

    # Extra edge cases
    mf = MedianFinder()
    for n in [-5, -5, 100000, -100000]:
        mf.addNum(n)
    print("Edge case median:", mf.findMedian())  # sorted: [-100000, -5, -5, 100000] -> -5.0
    assert mf.findMedian() == -5.0

    # Randomized check against Python's statistics.median
    for _ in range(200):
        mf = MedianFinder()
        data = []
        for _ in range(random.randint(1, 100)):
            n = random.randint(-100_000, 100_000)
            data.append(n)
            mf.addNum(n)
            assert mf.findMedian() == statistics.median(data)

    print("All tests passed!")