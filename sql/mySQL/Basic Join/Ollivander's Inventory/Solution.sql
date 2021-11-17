SELECT w1.id, p1.age, w1.coins_needed, w1.Power
FROM WANDS AS w1 INNER JOIN Wands_Property AS p1
ON w1.code = p1.code
WHERE p1.is_evil = 0 AND
w1.coins_needed = (
                        SELECT min(w2.coins_needed) 
                        from WANDS AS w2 INNER JOIN Wands_Property AS p2
                        ON w2.code = p2.code
                        WHERE p1.age = p2.age AND w1.Power = w2.power
                  )
order by w1.Power desc, p1.age desc
