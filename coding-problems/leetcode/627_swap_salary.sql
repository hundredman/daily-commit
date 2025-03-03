-- 문제: Write a solution to swap all 'f' and 'm' values (i.e., change all 'f' values to 'm' and vice versa)
-- with a single update statement and no intermediate temporary tables.
-- 문제 링크: https://leetcode.com/problems/swap-salary/

UPDATE Salary
SET sex = CASE
              WHEN sex = 'm' THEN 'f'
              WHEN sex = 'f' THEN 'm'
          END;
