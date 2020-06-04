"""

Write a SQL query to delete all duplicate email entries in a table named Person, keeping only unique emails based on its smallest Id.

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+
Id is the primary key column for this table.
For example, after running your query, the above Person table should have the following rows:

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+
Note:

Your output is the whole Person table after executing your sql. Use delete statement.

https://leetcode.com/problems/delete-duplicate-emails/

@author Mina HE
"""


# Write your MySQL query statement below
DELETE FROM Person WHERE Id NOT IN
(
    SELECT Id FROM
    (
        SELECT min(Id) AS Id
        FROM Person
        GROUP BY Email
    ) tab
)


"""
Runtime: 1761 ms, faster than 52.89% of Python online submissions.
Memory Usage: 0B, less than 100.00% of Python online submissions.
"""
