-- 문제: Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
-- 문제 링크: https://leetcode.com/problems/delete-duplicate-emails/

DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;
