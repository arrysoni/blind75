"""
Reorder Linked List
Medium

You are given the head of a singly linked-list.

The positions of a linked list of length = 7 for example, can intially be represented as:

[0, 1, 2, 3, 4, 5, 6]

Reorder the nodes of the linked list to be in the following order:

[0, 6, 1, 5, 2, 4, 3]

In the general case, label the nodes by their original zero-based positions from 0 to n - 1. After reordering, those original positions appear in this order:

[0, n-1, 1, n-2, 2, n-3, ...]

These numbers represent node positions, not the values stored in the nodes.

You may not modify the values in the list's nodes, but instead you must reorder the nodes themselves.

Example 1:
Input: head = [2,4,6,8]
Output: [2,8,4,6]

Example 2:
Input: head = [2,4,6,8,10]
Output: [2,10,4,8,6]

Constraints:
1 <= Length of the list <= 1000.
1 <= Node.val <= 1000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ---------- visual helpers ----------
 
def draw(head, pointers=None, title=""):
    """
    Prints the list with pointer labels underneath, e.g.
 
        2 -> 4 -> 6 -> 8 -> None
        ^         ^
        slow      fast
    """
    pointers = pointers or {}
    cells, positions = [], {}
    col, node, seen = 0, head, set()
 
    while node and id(node) not in seen:   # guard against accidental cycles
        seen.add(id(node))
        positions[id(node)] = col
        s = str(node.val)
        cells.append(s)
        col += len(s) + 4                   # width of "val -> "
        node = node.next
 
    line = " -> ".join(cells) + (" -> None" if cells else "None")
    if node:                                # we stopped because of a cycle
        line += " -> (cycle!)"
 
    if title:
        print(f"  {title}")
    print("    " + line)
 
    # Group labels by column so two pointers on one node share a caret
    by_col = {}
    for name, target in pointers.items():
        if target is None:
            continue
        c = positions.get(id(target))
        if c is not None:
            by_col.setdefault(c, []).append(name)
 
    if by_col:
        width = max(len(line), max(by_col) + 1)
        caret = [" "] * width
        for c in by_col:
            caret[c] = "^"
        print("    " + "".join(caret).rstrip())
        label_line = ""
        for c in sorted(by_col):
            label = "/".join(by_col[c])
            label_line = label_line.ljust(c) + label + " "
        print("    " + label_line.rstrip())
 
    # Pointers that are None get listed separately
    nulls = [n for n, t in pointers.items() if t is None]
    if nulls:
        print("    " + ", ".join(f"{n} = None" for n in nulls))
    print()
 
 
def section(title):
    print("=" * 50)
    print(title)
    print("=" * 50)
 
 
# ---------- solution with prints ----------
 
class Solution:
    def reorderList(self, head):
        section("START")
        draw(head, {"head": head})
 
        # 1. Find middle (slow ends at end of first half)
        section("STEP 1: find the middle (slow/fast pointers)")
        slow, fast = head, head.next
        step = 0
        draw(head, {"slow": slow, "fast": fast}, f"init")
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            step += 1
            draw(head, {"slow": slow, "fast": fast},
                 f"move {step}: slow +1, fast +2")
        print(f"  -> slow stopped at {slow.val}; the first half ends here\n")
 
        # 2. Reverse second half and cut the list in two
        section("STEP 2: cut the list and reverse the second half")
        second = slow.next
        slow.next = None
        draw(head, {"head": head, "slow": slow}, "first half (cut after slow)")
        draw(second, {"second": second}, "second half (before reversing)")
 
        prev = None
        step = 0
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
            step += 1
            print(f"  reverse step {step}:")
            draw(prev, {"prev": prev}, "reversed so far")
            draw(second, {"second": second}, "still to reverse")
 
        # 3. Merge the two halves alternately
        section("STEP 3: merge the halves alternately")
        first, second = head, prev
        draw(first, {"first": first}, "first half")
        draw(second, {"second": second}, "reversed second half")
 
        step = 0
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            step += 1
            print(f"  merge step {step}: linked {first.val} -> {second.val}"
                  f" -> {tmp1.val if tmp1 else 'None'}")
            first, second = tmp1, tmp2
            draw(head, {"head": head, "first": first}, "list from head")
            draw(second, {"second": second}, "second half remaining")
 
        section("RESULT")
        draw(head, {"head": head})
 
 
# ---------- test driver ----------
 
def build(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next
 
 
def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out
 
 
if __name__ == "__main__":
    tests = [
        ([2, 4, 6, 8], [2, 8, 4, 6]),
        ([2, 4, 6, 8, 10], [2, 10, 4, 8, 6]),
    ]
    for values, expected in tests:
        print("\n" + "#" * 50)
        print(f"# INPUT: {values}")
        print("#" * 50 + "\n")
        head = build(values)
        Solution().reorderList(head)
        got = to_list(head)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: got {got}, expected {expected}")
 