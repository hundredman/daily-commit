-- 문제: Write a solution to find the first login date for each player.
-- 문제 링크: https://leetcode.com/problems/game-play-analysis-i/

SELECT player_id, MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;
