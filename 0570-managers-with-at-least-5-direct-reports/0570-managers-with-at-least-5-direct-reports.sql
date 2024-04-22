# Write your MySQL query statement below
SELECT ma.name 
FROM Employee as em 
INNER JOIN Employee as ma
ON ma.Id=em.managerId
GROUP BY em.managerId
HAVING COUNT(em.id)>=5;

