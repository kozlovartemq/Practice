SELECT CEIL(AVG(SALARY) - AVG(REPLACE(SALARY, '0', ''))) FROM employees

/*
CEIL - Функция округления числа
REPLACE - Функция замены (где?, что?, на что?)
*/
