select sum(round(LAT_N,4)) AS res
from (select ROW_NUMBER() OVER (order by LAT_N) AS ROW_, LAT_N from STATION order by LAT_N) AS New_table2
WHERE 
ROW_ = (select count(LAT_N) div 2 + 1 
  from (select ROW_, LAT_N from STATION order by LAT_N) AS New_table3) OR
ROW_ = (select IF(count(LAT_N) % 2 = 0, count(LAT_N) / 2 + 1, 0) 
  from (select ROW_, LAT_N from STATION order by LAT_N) AS New_table4)
  
  /*
  ROW_NUMBER() OVER(...) - used for numbering lines
  To calculate the median, I am checking the value of the number of lines for parity
  DIV - Integer division
  OR - to create the second value in case there is the value of the number of lines is even
  IF(expression, 'true', 'false') - checking the value of the number of lines for parity
  */
