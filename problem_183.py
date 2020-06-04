"""
Suppose that a website contains two tables, the Customers table and the Orders table.
Write a SQL query to find all customers who never order anything.

Table: Customers.

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Table: Orders.

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
Using the above tables as example, return the following:

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

https://leetcode.com/problems/customers-who-never-order/

@author Mina HE
"""


# Write your MySQL query statement below
WITH tab AS
(Select o.Id AS OrderId, Name
FROM Customers AS c LEFT JOIN Orders AS o
ON c.Id = o.CustomerId
)
SELECT Name AS Customers
FROM tab
WHERE OrderId is Null


"""
Runtime: 448 ms, faster than 69.17% of Python online submissions.
Memory Usage: 0B, less than 100.00% of Python online submissions.
"""
