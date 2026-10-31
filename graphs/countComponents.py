"""
Number of Connected Components in an Undirected Graph
Medium

You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

Example 1:
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n
0 <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.
"""
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # Create adj. list node:[neighbour]
        adj = {i: [] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i):
            if i in visit:
                return
            visit.add(i)
            for j in adj[i]:
                dfs(j)

        count = 0
        for i in range(n):
            if i not in visit:   # not reached by any earlier DFS → new component
                dfs(i)
                count += 1
        return count


if __name__ == "__main__":
    sol = Solution()
    print(sol.countComponents(5, [[0, 1], [1, 2], [3, 4]]))          # expected 2
    print(sol.countComponents(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))  # expected 1
    print(sol.countComponents(3, []))                                # expected 3
