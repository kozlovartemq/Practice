select 
case 
    WHEN Grades.Grade >= 8                   /* IF could have been used instead of CASE: 
    THEN Students.Name                          IF(Grades.Grade >= 8, Students.Name, null)  */
END AS Names,
Grades.Grade, Students.Marks from Students
Inner Join Grades                             
ON Students.Marks >= Grades.MIN_Mark AND      /* BETWEEN could have been used: 
    Students.Marks <= Grades.MAX_Mark            BETWEEN Grades.MIN_Mark AND Grades.MAX_Mark */
order by Grades.Grade desc, Names asc
