-- 문제: Write a solution to find all the pairs (actor_id, director_id)
-- where the actor has cooperated with the director at least three times.
-- 문제 링크: https://leetcode.com/problems/actors-and-directors-who-cooperated-at-least-three-times/

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING count(*) >= 3;
