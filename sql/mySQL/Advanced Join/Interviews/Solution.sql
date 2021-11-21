select C.contest_id, C.hacker_id, C.name, sum(sumtable.ts) AS S_ts, sum(sumtable.tas) AS S_tas, sum(vs.tv) AS S_tv1, sum(vs.tuv) AS S_tuv1
from Contests AS C
INNER JOIN Colleges AS Col
ON C.contest_id = Col.contest_id
INNER JOIN Challenges AS CH
ON CH.college_id = Col.college_id
LEFT JOIN
    (
    select ss.challenge_id AS id, SUM(total_submissions) AS ts, SUM(total_accepted_submissions) AS tas
    from Submission_Stats AS ss
    group by ss.challenge_id  
    ) AS sumtable                                       /*  Adding the SUM values of submissions at that Challenges can be different */
ON CH.challenge_id = sumtable.id     
LEFT JOIN 
    (
    select v.challenge_id AS id, SUM(total_views) AS tv, SUM(total_unique_views) AS tuv
    from View_stats AS v 
    group by v.challenge_id
    ) AS vs                                             /*  Adding the SUM values of views at that Challenges can be different */
ON ch.challenge_id = vs.id
group by C.contest_id, C.hacker_id, C.name
having S_ts != 0 OR                                     /* Exluding rows, where all the SUM values = 0 */
       S_tas != 0 OR
       S_tv1 != 0 OR
       S_tuv1 != 0
order by c.contest_id
