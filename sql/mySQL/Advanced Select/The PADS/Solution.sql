select
case when Occupation = "Doctor"   /* CASE - проверяет истинность набора условий /*
    THEN CONCAT(name, '(D)')      /* CONCAT() = print() - вывод данных, разделитель "," /*
    when Occupation = "Actor"
    THEN CONCAT(name, '(A)')
    when Occupation = "Singer"
    THEN CONCAT(name, '(S)')
    when Occupation = "Professor"
    THEN CONCAT(name, '(P)')
END
from OCCUPATIONS order by name;

select CONCAT('There are a total of ', count(occupation), ' ', lower(occupation), 's.')
from OCCUPATIONS
group by occupation order by count(occupation), occupation; /* group by - агрегирует данные для count() */
