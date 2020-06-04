"""
Write a SQL query to find all duplicate emails in a table named Person.

+----+---------+
| Id | Email   |
+----+---------+
| 1  | a@b.com |
| 2  | c@d.com |
| 3  | a@b.com |
+----+---------+
For example, your query should return the following for the above table:

+---------+
| Email   |
+---------+
| a@b.com |
+---------+
Note: All emails are in lowercase.

https://leetcode.com/problems/duplicate-emails/

@author Mina HE
"""


# Write your MySQL query statement below
SELECT Email from Person
GROUP BY Email
HAVING COUNT(1)>1


"""
Runtime: 858 ms, faster than 13.07% of Python online submissions.
Memory Usage: 0B, less than 100.00% of Python online submissions.
"""
