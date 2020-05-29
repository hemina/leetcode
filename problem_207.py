"""
There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.


Constraints:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
1 <= numCourses <= 10^5

https://leetcode.com/problems/course-schedule/

@author Mina HE
"""


class Solution:
    def helper(self, course):
        if self.finish[course] == 1:  # visiting
            return False
        if self.finish[course] == -1:  # already finished course
            return True
        # when self.finish[course] == 0, for unvisited course
        self.finish[course] = 1  # mark as visiting
        if self.prerequisites[course]:  # when prerequisites for this course is not None
            for base in self.prerequisites[course]:
                if not self.helper(base):
                    return False
        self.finish[course] = -1  # mark as finished course
        return True

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.prerequisites = [[] for i in range(numCourses)]
        self.finish = [0 for i in range(numCourses)]
        for course, base in prerequisites:
            self.prerequisites[course].append(base)
        len_prerequisite = [len(prerequisite) for prerequisite in self.prerequisites]
        if min(len_prerequisite) > 0:
            return False
        for i in range(numCourses):
            if not self.helper(i):
                return False
        return True


"""
Runtime: 92 ms, faster than 97.11% of Python online submissions.
Memory Usage: 15.2 MB, less than 65.31% of Python online submissions.
"""
