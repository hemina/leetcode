"""
We are given two sentences A and B.  (A sentence is a string of space separated words.  Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Return a list of all uncommon words.

You may return the list in any order.



Example 1:

Input: A = "this apple is sweet", B = "this apple is sour"
Output: ["sweet","sour"]
Example 2:

Input: A = "apple apple", B = "banana"
Output: ["banana"]


Note:

0 <= A.length <= 200
0 <= B.length <= 200
A and B both contain only spaces and lowercase letters.

https://leetcode.com/problems/uncommon-words-from-two-sentences/

@author Mina HE
"""


class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        ans = []
        wordlist_A = A.split()
        wordlist_B = B.split()
        possible_words_in_A = set(wordlist_A) - set(wordlist_B)
        possible_words_in_B = set(wordlist_B) - set(wordlist_A)
        for word in possible_words_in_A:
            wordlist_A.remove(word)
            if word not in wordlist_A:
                ans.append(word)
        for word in possible_words_in_B:
            wordlist_B.remove(word)
            if word not in wordlist_B:
                ans.append(word)
        return ans


"""
Runtime: 8 ms, faster than 99.11%  of Python online submissions.
Memory Usage: 11.7 MB, less than 36.36%  of Python online submissions.
Complexity: O(nˆ2)
"""
