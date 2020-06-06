"""
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k),
where h is the height of the person and k is the number of people in front of this person
who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

https://leetcode.com/problems/queue-reconstruction-by-height/

@author Mina HE
"""


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people.sort(key=lambda people: (people[0], -people[1]))
        queue = []
        while people:
            h, k = people.pop()
            queue.insert(k, [h, k])
        return queue


"""
Runtime: 92 ms, faster than 95.80% of Python online submissions.
Memory Usage: 14.1 MB, less than 70.82% of Python online submissions.
Complexity: O(nlogn) for pickIndex, O(n) for init.
"""
