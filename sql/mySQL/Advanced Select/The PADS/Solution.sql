select
case when Occupation = "Doctor"   /* CASE - goes through conditions and return a value when the first condition is met */
    THEN CONCAT(name, '(D)')      /* CONCAT() - function adds two or more expressions together, separator "," */
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
group by occupation order by count(occupation), occupation; /* group by - aggregate data for count() */
