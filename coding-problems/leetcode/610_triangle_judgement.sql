-- 문제: Report for every three line segments whether they can form a triangle.
-- 문제 링크: https://leetcode.com/problems/triangle-judgement/

SELECT x, y, z,
       CASE
           WHEN x + y > z AND x + z > y AND y + z > x
           THEN 'Yes'
           ELSE 'No'
           END AS triangle
FROM Triangle;
