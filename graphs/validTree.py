"""
Graph Valid Tree
Medium

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge is a pair of nodes), write a function to check whether these edges make up a valid tree.

Example 1:
Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
Output: true

Example 2:
Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
Output: false

Note:
You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Constraints:
1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= a_i, b_i < n
a_i != b_i
There are no self-loops or repeated edges.
"""
from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if not n:
            return True

        # Create adj. list node:[neighbour]
        adj = {i:[] for i in range(n)}

        # Fill in the adj. list
        for n1,n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(i, prev):

            if i in visit:
                return False

            visit.add(i)

            # For neighbours of i 
            for j in adj[i]:
                if j == prev: # The node has no more neighnours except prev
                    continue

                # If my neighbour found a cycle, then I have a cycle too. Stop and report it upward.”
                if not dfs(j,i):
                    return False
                
            return True
        
        # Conditions for valid tree
        return dfs(0, -1) and n == len(visit)


if __name__ == "__main__":
    sol = Solution()
    print(sol.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))        # expected True
    print(sol.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))  # expected False

"""
Execution Pattern:
dfs(0, -1)        visit {0}, neighbours [1, 2]
  dfs(1, 0)       visit {0,1}, neighbours [0, 2]; 0 is prev, so skip it
    dfs(2, 1)     visit {0,1,2}, neighbours [1, 0]; 1 is prev, so skip it
      dfs(0, 2)   0 is already in visit → return False   ← cycle found here
    dfs(2,1) sees False → return False
  dfs(1,0) sees False → return False
dfs(0,-1) sees False → return False
"""
        
        