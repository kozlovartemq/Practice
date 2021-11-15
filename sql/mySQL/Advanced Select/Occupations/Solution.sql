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
    min/max - used to aggregate data (to use group by)
    min() for string data will show a string that starts with a letter that is as early as possible in the alphabet, max() - opposite
    ROW_NUMBER() OVER(...) - used for numbering lines
    PARTITION BY - used to divide data into multiple subsections
    order by - indicate the order in which the lines will be located for subsequent numbering
    group by - groups together rows with the same values for processing
    */
