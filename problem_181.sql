"""
SQL Schema
Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

https://leetcode.com/problems/employees-earning-more-than-their-managers/

@author Mina HE
"""

select E1.name as Employee from 
Employee as E1, Employee as E2 
where E1.managerId = E2.id and E1.salary > E2.salary