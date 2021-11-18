Select hh.hacker_id, hh.name, sum(table_.maxscore) AS tscore  /* tscore - total score (sum) of a multiple challenges by a single hacker */
FROM HACKERS AS hh
INNER JOIN
(
select h.hacker_id AS id, max(s.score) AS maxscore
from Hackers AS h
Inner JOIN Submissions AS s
ON h.hacker_id = s.hacker_id
group by s.challenge_id, h.hacker_id
) AS table_                                       /* table_ is a table contains maxscore for a single challenge by a single hacker*/
ON hh.hacker_id = table_.id
group by hh.hacker_id, hh.name
having tscore > 0                     /* having is used to interact with resulted aggregated data and to support aliases, so no need to sum() again to filter */
order by tscore desc, hh.hacker_id    /* WHERE is used to interact with primary data and doesn't support aliases */
