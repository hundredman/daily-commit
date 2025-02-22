-- 문제: Find the names of the customer that are not referred by the customer with id = 2.
-- 문제 링크: https://leetcode.com/problems/find-customer-referee/

SELECT name
FROM Customer
WHERE referee_id != 2 OR referee_id IS NULL;
