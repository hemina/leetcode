"""
We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.



Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation:
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.


Note:

1 <= A.length <= 10000
-10000 <= A[i] <= 10000
1 <= queries.length <= 10000
-10000 <= queries[i][0] <= 10000
0 <= queries[i][1] < A.length

https://leetcode.com/problems/sum-of-even-numbers-after-queries/

@author Mina HE
"""


class Solution(object):
    def sumEvenAfterQueries(self, A, queries):
        """
        :type A: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        answer = []
        s = sum([item if item%2 == 0 else 0 for item in A])
        for i, query in enumerate(queries):
            old_val = A[query[1]]
            A[query[1]] = new_val = A[query[1]]+query[0]
            old_in_sum = old_val if old_val%2 == 0 else 0
            new_in_sum = new_val if new_val%2 == 0 else 0
            s = s + new_in_sum - old_in_sum
            answer.append(s)
        return answer


"""
Runtime: 480 ms, faster than 54.80% of Python online submissions.
Memory Usage: 18.1 MB, less than 50.00% of Python online submissions.
Complexity: O(m+n)
"""
