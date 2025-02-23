-- 문제: Write a solution to find the customer_number for the customer who has placed the largest number of orders.
-- 문제 링크: https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(*) DESC
LIMIT 1;
