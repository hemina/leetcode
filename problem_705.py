"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);
hashSet.add(2);
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);
hashSet.contains(2);    // returns true
hashSet.remove(2);
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.

https://leetcode.com/problems/design-hashset

@author Mina HE
"""


class MyHashSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hash.discard(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return True if key in self.hash else False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


"""
Runtime: 148 ms, faster than 98.91% of Python online submissions.
Memory Usage: 17.3 MB, less than 75.00% of Python online submissions.
"""
