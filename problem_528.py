"""
Given an array w of positive integers, where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.
Example 1:

Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]
Example 2:

Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]
Explanation of Input Syntax:

The input is two lists: the subroutines called and their arguments.
Solution's constructor has one argument, the array w. pickIndex has no arguments.
Arguments are always wrapped with a list, even if there aren't any.

https://leetcode.com/problems/random-pick-with-weight/

@author Mina HE
"""


class Solution:
    def __init__(self, w: List[int]):
        self.sum_list = []
        self.len_w = len(w)
        tmp = 0
        for num in w:
            tmp += num
            self.sum_list.append(tmp)

    def pickIndex(self) -> int:
        x = random.random()*self.sum_list[-1]
        n = self.len_w//2
        first = 0
        last = self.len_w
        while first < last:
            if self.sum_list[n] >= x:
                if self.sum_list[n-1] <= x:
                    return n
                else:
                    last = n
                    n = (n - first)//2 + first
            else:
                first = n
                n = (last - n)//2 + n
        return first

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


"""
Runtime: 256 ms, faster than 69.71% of Python online submissions.
Memory Usage: 18.1 MB, less than 88.83% of Python online submissions.
Complexity: O(logn) for pickIndex, O(n) for init.
"""
