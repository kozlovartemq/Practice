SELECT N,
CASE 
    WHEN p IS null
        THEN 'Root'
    WHEN N IN (SELECT DISTINCT P from BST) /* SELECT DISTINCT - interact only with non-duplicate data */
        THEN 'Inner'
    ELSE 'Leaf'
END
FROM BST ORDER BY N;
