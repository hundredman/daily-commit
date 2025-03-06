-- 문제: Write a solution to report the product_name, year, and price for each sale_id in the Sales table.
-- 문제 링크: https://leetcode.com/problems/product-sales-analysis-i/

SELECT p.product_name, s.year, s.price
FROM Sales s JOIN Product p
ON p.product_id = s.product_id;
