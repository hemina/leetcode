"""
There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.


Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

https://leetcode.com/problems/cheapest-flights-within-k-stops/

@author Mina HE
"""


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        price_table = [float('inf') for i in range(n)]
        price_table[src] = 0
        for source, destination, price in flights:
            if source == src:  # mark the price of every direct flight from the starting city
                price_table[destination] = price
        current_table = price_table[:]
        for i in range(K):
            for source, destination, price in flights:  # mark price from src to every destination
                current_table[destination] = min(current_table[destination], price_table[source]+price)
            price_table = current_table[:]

        if price_table[dst] == float('inf'):
            return -1
        return price_table[dst]


"""
Runtime: 152 ms, faster than 31.24% of Python online submissions.
Memory Usage: 14.5 MB, less than 93.35% of Python online submissions.
Complexity: O(k*m), m is the amount of flights, k is the number of stops
"""
