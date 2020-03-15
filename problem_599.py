"""
Suppose Andy and Doris want to choose a restaurant for dinner,
and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum.
If there is a choice tie between answers, output all of them with no order requirement.
You could assume there always exists an answer.

Example 1:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:
Input:
["Shogun", "Tapioca Express", "Burger King", "KFC"]
["KFC", "Shogun", "Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
Note:
The length of both lists will be in the range of [1, 1000].
The length of strings in both lists will be in the range of [1, 30].
The index is starting from 0 to the list length minus 1.
No duplicates in both lists.

https://leetcode.com/problems/minimum-index-sum-of-two-lists

@author Mina HE
"""


def findRestaurant(self, list1, list2):
    """
    :type list1: List[str]
    :type list2: List[str]
    :rtype: List[str]
    """

    MIN = float('inf')
    final_restaurant = []

    dict1 = {restaurant: ind for ind, restaurant in enumerate(list1)}
    dict2 = {restaurant: ind + dict1[restaurant] for ind, restaurant in enumerate(list2) if restaurant in dict1}

    for val, ind in dict2.items():
        if ind < MIN:
            final_restaurant = [val]
            MIN = ind
        elif ind == MIN:
            final_restaurant.append(val)
    return final_restaurant


"""
Runtime: 116 ms, faster than 86.06% of Python online submissions.
Memory Usage: 12.2 MB, less than 50.00% of Python online submissions.
Complexity: O(m*n)
"""
