"""
Given a circular array C of integers represented by A, find the maximum possible sum of a non-empty subarray of C.

Here, a circular array means the end of the array connects to the beginning of the array.
(Formally, C[i] = A[i] when 0 <= i < A.length, and C[i+A.length] = C[i] when i >= 0.)

Also, a subarray may only include each element of the fixed buffer A at most once.
(Formally, for a subarray C[i], C[i+1], ..., C[j],
there does not exist i <= k1, k2 <= j with k1 % A.length = k2 % A.length.)



Example 1:

Input: [1,-2,3,-2]
Output: 3
Explanation: Subarray [3] has maximum sum 3
Example 2:

Input: [5,-3,5]
Output: 10
Explanation: Subarray [5,5] has maximum sum 5 + 5 = 10
Example 3:

Input: [3,-1,2,-1]
Output: 4
Explanation: Subarray [2,-1,3] has maximum sum 2 + (-1) + 3 = 4
Example 4:

Input: [3,-2,2,-3]
Output: 3
Explanation: Subarray [3] and [3,-2,2] both have maximum sum 3
Example 5:

Input: [-2,-3,-1]
Output: -1
Explanation: Subarray [-1] has maximum sum -1


Note:

-30000 <= A[i] <= 30000
1 <= A.length <= 30000

https://leetcode.com/problems/maximum-sum-circular-subarray/

@author Mina HE
"""


class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_ending_here = max_so_far = A[0]
        min_ending_here = min_so_far = A[0]
        s = sum(A)
        for num in A[1:]:
            max_ending_here = max(num, max_ending_here+num) # if precedent sum<0, forget all
            max_so_far = max(max_so_far, max_ending_here)
            min_ending_here = min(num, min_ending_here+num) # if precedent sum>0, forget all
            min_so_far = min(min_so_far, min_ending_here)
        if s == min_so_far: # when all values are negative
            return max_so_far
        return max(s-min_so_far, max_so_far)


"""
Runtime: 580 ms, faster than 67.92% of Python online submissions.
Memory Usage: 18 MB, less than 100.00% of Python online submissions.
Complexity: O(n)
"""
