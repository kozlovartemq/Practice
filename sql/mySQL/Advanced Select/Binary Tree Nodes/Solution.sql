SELECT N,
CASE 
    WHEN p IS null
        THEN 'Root'
    WHEN N IN (SELECT DISTINCT P from BST) /* SELECT DISTINCT - выбор неповторяющихся данных */
        THEN 'Inner'
    ELSE 'Leaf'
END
FROM BST ORDER BY N;
