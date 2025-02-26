-- 문제: Write a solution to find all the classes that have at least five students.
-- 문제 링크: https://leetcode.com/problems/classes-more-than-5-students/

SELECT class
FROM courses
GROUP BY class
HAVING count(*) >= 5;
