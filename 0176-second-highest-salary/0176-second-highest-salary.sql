# Write your MySQL query statement below
SELECT max(e1.salary) as SecondHighestSalary
FROM Employee e1 join Employee e2 ON e1.salary<e2.salary;