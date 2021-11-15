select ROUND(MAX(LAT_N) - MIN(LAT_N) + MAX(LONG_W) - MIN(LONG_W), 4) from STATION /* round(expression , N) - round to a scale of N decimal places */
