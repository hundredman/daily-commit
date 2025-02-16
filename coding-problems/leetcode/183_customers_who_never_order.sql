-- 문제: Write a solution to find all customers who never order anything.
-- 문제 링크: https://leetcode.com/problems/customers-who-never-order/

SELECT Customers.name AS Customers FROM Customers
LEFT JOIN Orders ON Customers.id = Orders.customerId
WHERE Orders.customerId IS NULL;
