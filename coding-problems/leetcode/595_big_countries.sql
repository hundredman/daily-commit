-- 문제: Write a solution to find the name, population, and area of the big countries.
-- 문제 링크: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;
