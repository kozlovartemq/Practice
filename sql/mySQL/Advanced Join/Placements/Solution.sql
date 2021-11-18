select s.name
from Students AS s
INNER JOIN FRIENDS AS f       /* Join Friend
ON s.ID = f.ID
INNER JOIN Packages AS p      /* Join ID's Salaries */
ON s.ID = p.ID
INNER JOIN Packages AS p2     /* Join Friend's Salaries */
ON f.Friend_ID = p2.ID
Where p.Salary < p2.Salary
order by p2.Salary
