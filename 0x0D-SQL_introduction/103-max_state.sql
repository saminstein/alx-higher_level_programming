-- displays the max temperature of each state (ordered by State name)

SELECT state, MAX(temperature) AS max_temp
FROM temperature
GROUP BY state;