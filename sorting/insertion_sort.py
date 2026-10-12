"""
Insertion Sort
Easy

Implement Insertion Sort and return intermediate states.
Insertion Sort is a simple sorting algorithm that builds the sorted list one element at a time, from left to right. It works by repeatedly taking an element from the unsorted portion and inserting it into its correct position in the sorted portion of the list.

Objective:
Given a list of key-value pairs, sort the list by key using Insertion Sort. Return a list of lists showing the state of the array after each insertion. If two key-value pairs have the same key, maintain their relative order in the sorted list.

Input:
pairs - a list of key-value pairs, where each key-value has an integer key and a string value. (0 <= pairs.length <= 100).

Example 1:
Input:
pairs = [(5, "apple"), (2, "banana"), (9, "cherry")]
Output:
[[(5, "apple"), (2, "banana"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")], 
 [(2, "banana"), (5, "apple"), (9, "cherry")]]

Notice that the output shows the state of the array after each insertion. The last state is the final sorted array. There should be pairs.length states in total.

Example 2:
Input:
pairs = [(3, "cat"), (3, "bird"), (2, "dog")]
Output:
[[(3, "cat"), (3, "bird"), (2, "dog")], 
 [(3, "cat"), (3, "bird"), (2, "dog")],
 [(2, "dog"), (3, "cat"), (3, "bird")]]
In this example, you can observe that the pairs with key=3 ("cat" and "bird") maintain their relative order, illustrating the stability of the Insertion Sort algorithm.
"""
import unittest
from typing import List


# ---- Provided by the judge (defined here so the file runs locally) ----
class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value

    # Only needed for local testing, so assertions and failure messages are readable
    def __eq__(self, other):
        return isinstance(other, Pair) and self.key == other.key and self.value == other.value

    def __repr__(self):
        return f"({self.key}, {self.value!r})"


# ---- Your solution ----
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        arr = list(pairs)

        for i in range(len(arr)):
            j = i - 1
            curr = arr[i]

            while j >= 0 and arr[j].key > curr.key:
                arr[j + 1] = arr[j]
                j -= 1

            arr[j + 1] = curr
            res.append(list(arr))

        return res


# ---- Helpers ----
def P(tuples):
    """[(5, 'a'), ...] -> [Pair(5, 'a'), ...]"""
    return [Pair(k, v) for k, v in tuples]


def states(tuple_states):
    """List of tuple-lists -> List of Pair-lists"""
    return [P(s) for s in tuple_states]


# ---- Tests ----
class TestInsertionSort(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_example_1(self):
        out = self.sol.insertionSort(P([(5, "apple"), (2, "banana"), (9, "cherry")]))
        expected = states([
            [(5, "apple"), (2, "banana"), (9, "cherry")],
            [(2, "banana"), (5, "apple"), (9, "cherry")],
            [(2, "banana"), (5, "apple"), (9, "cherry")],
        ])
        self.assertEqual(out, expected)

    def test_example_2_stability(self):
        out = self.sol.insertionSort(P([(3, "cat"), (3, "bird"), (2, "dog")]))
        expected = states([
            [(3, "cat"), (3, "bird"), (2, "dog")],
            [(3, "cat"), (3, "bird"), (2, "dog")],
            [(2, "dog"), (3, "cat"), (3, "bird")],
        ])
        self.assertEqual(out, expected)

    def test_empty(self):
        self.assertEqual(self.sol.insertionSort([]), [])

    def test_single_element(self):
        out = self.sol.insertionSort(P([(1, "a")]))
        self.assertEqual(out, states([[(1, "a")]]))

    def test_already_sorted(self):
        out = self.sol.insertionSort(P([(1, "a"), (2, "b"), (3, "c")]))
        expected = states([
            [(1, "a"), (2, "b"), (3, "c")],
            [(1, "a"), (2, "b"), (3, "c")],
            [(1, "a"), (2, "b"), (3, "c")],
        ])
        self.assertEqual(out, expected)

    def test_reverse_sorted(self):
        out = self.sol.insertionSort(P([(3, "c"), (2, "b"), (1, "a")]))
        expected = states([
            [(3, "c"), (2, "b"), (1, "a")],
            [(2, "b"), (3, "c"), (1, "a")],
            [(1, "a"), (2, "b"), (3, "c")],
        ])
        self.assertEqual(out, expected)

    def test_all_equal_keys(self):
        data = [(7, "a"), (7, "b"), (7, "c")]
        out = self.sol.insertionSort(P(data))
        self.assertEqual(out, states([data, data, data]))

    def test_interleaved_duplicates_stable(self):
        out = self.sol.insertionSort(P([(2, "a"), (1, "b"), (2, "c"), (1, "d")]))
        expected = states([
            [(2, "a"), (1, "b"), (2, "c"), (1, "d")],
            [(1, "b"), (2, "a"), (2, "c"), (1, "d")],
            [(1, "b"), (2, "a"), (2, "c"), (1, "d")],
            [(1, "b"), (1, "d"), (2, "a"), (2, "c")],
        ])
        self.assertEqual(out, expected)

    def test_negative_and_zero_keys(self):
        out = self.sol.insertionSort(P([(0, "z"), (-1, "y"), (-1, "x"), (5, "w")]))
        expected = states([
            [(0, "z"), (-1, "y"), (-1, "x"), (5, "w")],
            [(-1, "y"), (0, "z"), (-1, "x"), (5, "w")],
            [(-1, "y"), (-1, "x"), (0, "z"), (5, "w")],
            [(-1, "y"), (-1, "x"), (0, "z"), (5, "w")],
        ])
        self.assertEqual(out, expected)

    def test_number_of_states_equals_length(self):
        data = P([(4, "a"), (1, "b"), (3, "c"), (2, "d"), (5, "e")])
        self.assertEqual(len(self.sol.insertionSort(data)), len(data))

    def test_snapshots_are_independent(self):
        out = self.sol.insertionSort(P([(3, "c"), (2, "b"), (1, "a")]))
        # If snapshots shared one list, all states would equal the final one
        self.assertNotEqual(out[0], out[-1])
        self.assertIsNot(out[0], out[1])

    def test_input_not_mutated(self):
        data = P([(3, "c"), (2, "b"), (1, "a")])
        original = list(data)
        self.sol.insertionSort(data)
        self.assertEqual(data, original)

    def test_final_state_is_sorted_large(self):
        import random
        random.seed(0)
        data = P([(random.randint(-50, 50), str(i)) for i in range(100)])
        out = self.sol.insertionSort(data)
        self.assertEqual(len(out), 100)
        keys = [p.key for p in out[-1]]
        self.assertEqual(keys, sorted(keys))
        # Stability check against Python's stable sort
        self.assertEqual(out[-1], sorted(data, key=lambda p: p.key))


if __name__ == "__main__":
    unittest.main(verbosity=2)
