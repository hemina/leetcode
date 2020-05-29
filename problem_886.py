"""
Given a set of N people (numbered 1, 2, ..., N), we would like to split everyone into two groups of any size.

Each person may dislike some other people, and they should not go into the same group.

Formally, if dislikes[i] = [a, b], it means it is not allowed to put the people numbered a and b into the same group.

Return true if and only if it is possible to split everyone into two groups in this way.



Example 1:

Input: N = 4, dislikes = [[1,2],[1,3],[2,4]]
Output: true
Explanation: group1 [1,4], group2 [2,3]
Example 2:

Input: N = 3, dislikes = [[1,2],[1,3],[2,3]]
Output: false
Example 3:

Input: N = 5, dislikes = [[1,2],[2,3],[3,4],[4,5],[1,5]]
Output: false


Note:

1 <= N <= 2000
0 <= dislikes.length <= 10000
1 <= dislikes[i][j] <= N
dislikes[i][0] < dislikes[i][1]
There does not exist i != j for which dislikes[i] == dislikes[j].

https://leetcode.com/problems/possible-bipartition/

@author Mina HE
"""


class Solution(object):
    def helper(self, node, color):
        self.visited[node - 1] = 0  # mark as visited node
        nei = self.dislikes[node - 1]  # get all neighbor nodes
        if nei:  # if neighbor nodes list is not empty
            for node in nei:
                new_color = 1 - color  # the neighbor node is supposed to be in a new color
                current_color = self.colors[node - 1]  # check if the neighbor node got a color registered
                if current_color is not None:
                    if current_color != new_color:  # if the registered color is different with the current one
                        return False
                else:
                    self.colors[node - 1] = new_color  # register the new color

                if self.visited[node - 1] < 0:  # if the neighbor node's dislikes list is not visited yet
                    if not self.helper(node, new_color):
                        return False
        return True

    def possibleBipartition(self, N, dislikes):
        """
        :type N: int
        :type dislikes: List[List[int]]
        :rtype: bool
        """
        self.dislikes = [[] for i in range(N)]  # the list of dislikes for each node
        self.colors = [None for i in range(N)]  # set color to 0 or 1
        self.visited = [-1] * N  # set -1 for unvisited nodes, 0 for visited nodes
        for a, b in dislikes:
            self.dislikes[a - 1].append(b)
            self.dislikes[b - 1].append(a)

        while sum(self.visited) < 0:  # if there are unvisited nodes
            node = self.visited.index(-1) + 1  # get the position of the first unvisited node
            if not self.helper(node, 0):
                return False
        return True


"""
Runtime: 644 ms, faster than 90.92% of Python online submissions.
Memory Usage: 18.5 MB, less than 100.00% of Python online submissions.
"""
