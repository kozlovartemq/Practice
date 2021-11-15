select distinct city from STATION
WHERE city not rlike '^[aouie]|[aouie]$'
/* 
distinct - remove repetitions
RLIKE - "regular expressions" allows to use [range] ARE not case sensitive
        ^ - beginning
        $ - end of string
        | - OR
        . - any character
        a+ - Match any sequence of one or more a characters
        a? - Match either zero or one a character
        a* - Match any sequence of zero or more a characters

*/
