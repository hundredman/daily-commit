-- 문제: Write a solution to find the employees who earn more than their managers.
-- 문제 링크: https://leetcode.com/problems/employees-earning-more-than-their-managers/

SELECT a.name AS Employee
FROM Employee a, Employee b
WHERE a.managerId = b.id AND a.salary > b.salary;
