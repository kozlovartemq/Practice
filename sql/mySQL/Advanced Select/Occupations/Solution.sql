select 
MIN(case when Occupation = "Doctor" 
    THEN Name
END) AS Doctors,
MIN(case when Occupation = "Professor" 
    THEN Name
END) AS Professors,
MIN(case when Occupation = "Singer" 
    THEN Name
END) AS Singers,
MAX(case when Occupation = "Actor" 
    THEN Name
END) AS Actors
FROM (select ROW_NUMBER() OVER (PARTITION BY Occupation order by NAME) AS ROW_, NAME, Occupation
FROM OCCUPATIONS) AS NewTable 
group by ROW_
    /*  
    min/max для агрегирования данных(чтобы использовать group by)
    min() для строковых данных покажет строку, которая начинается с буквы, которая находится как можно раньше в алфавите, max() - противоположно
    ROW_NUMBER() OVER(...) - используется для пронумеровки строк
    PARTITION BY - используется для разделения данных на несколько подразделов
    order by - настроить, в каком порядке будут располагаться строки для последующей нумеровки
    group by - обрабатывает вместе строки с одинаковыми значениями
    */
