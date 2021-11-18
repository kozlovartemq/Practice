Select hh.hacker_id, hh.name, sum(table_.maxscore) AS tscore
FROM HACKERS AS hh
INNER JOIN
(
select h.hacker_id AS id, max(s.score) AS maxscore
from Hackers AS h
Inner JOIN Submissions AS s
ON h.hacker_id = s.hacker_id
group by s.challenge_id, h.hacker_id
) AS table_
ON hh.hacker_id = table_.id
group by hh.hacker_id, hh.name
having tscore > 0
order by tscore desc, hh.hacker_id
