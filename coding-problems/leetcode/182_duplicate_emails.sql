-- 문제: Write a solution to report all the duplicate emails.
-- Note that it's guaranteed that the email field is not NULL.
-- 문제 링크: https://leetcode.com/problems/duplicate-emails/

SELECT email FROM Person
GROUP BY email
HAVING COUNT(email) > 1;
