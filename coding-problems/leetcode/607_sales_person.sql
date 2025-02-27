-- 문제: Write a solution to find the names of all the salespersons
-- who did not have any orders related to the company with the name "RED".
-- 문제 링크: https://leetcode.com/problems/sales-person/

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT DISTINCT sales_id
    FROM Orders
    WHERE com_id = (SELECT com_id FROM Company WHERE name = 'RED')
);
