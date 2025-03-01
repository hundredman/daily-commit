-- 문제: Find the largest single number. If there is no single number, report null.
-- 문제 링크: https://leetcode.com/problems/biggest-single-number/

SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);
