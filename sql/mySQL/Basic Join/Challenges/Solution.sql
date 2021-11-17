select RES_TABLE.id, RES_TABLE.n, RES_TABLE.res
FROM
        (
        SELECT h.hacker_id AS id, h.name AS n, count(ch.hacker_id) AS res
        FROM Hackers AS h INNER JOIN Challenges AS ch
        ON h.hacker_id = ch.hacker_id
        group by ch.hacker_id, h.name
        order by res desc
        ) AS RES_TABLE                                                        /* RES_TABLE, tablee - The table with unfiltered results */
INNER JOIN
        (
        select tablee.res AS ress, count(tablee.res) AS ReplyCOUNT
        FROM
                (
                SELECT h.hacker_id, h.name, count(ch.hacker_id) AS res
                FROM Hackers AS h INNER JOIN Challenges AS ch
                ON h.hacker_id = ch.hacker_id
                group by ch.hacker_id, h.name
                order by res desc
                ) AS tablee
        group by tablee.res 
        ) AS RE_TABLE                                                         /* RES_TABLE - The table contains a match of repeated rows with the same values of count(ch.hacker_id)*/
ON RE_TABLE.ress = RES_TABLE.res
WHERE
RES_TABLE.res = 
        (
        select max(RES_TABLE1.res)
        FROM
                (
                SELECT h.hacker_id AS id, h.name, count(ch.hacker_id) AS res
                FROM Hackers AS h INNER JOIN Challenges AS ch
                ON h.hacker_id = ch.hacker_id
                group by ch.hacker_id, h.name
                order by res desc
                ) AS RES_TABLE1
                )
OR
(
RES_TABLE.res != 
        (
        select max(RES_TABLE1.res)
        FROM
                (
                SELECT h.hacker_id AS id, h.name, count(ch.hacker_id) AS res
                FROM Hackers AS h INNER JOIN Challenges AS ch
                ON h.hacker_id = ch.hacker_id
                group by ch.hacker_id, h.name
                order by res desc
                ) AS RES_TABLE1
         )
AND ReplyCOUNT = 1
)
order by RES_TABLE.res desc, RES_TABLE.id
