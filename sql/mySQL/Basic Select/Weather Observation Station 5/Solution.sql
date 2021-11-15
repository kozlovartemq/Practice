select city, length(city) from STATION /* length() - func that counts the number of characters */
order by length(city), city limit 1;   /* limit - the number of the rows to output */
select city, length(city) from STATION
order by length(city) desc, city asc limit 1; /* desc - descending, asc - ascending */
