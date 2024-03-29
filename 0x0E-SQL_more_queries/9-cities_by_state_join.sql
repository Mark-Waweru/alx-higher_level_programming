-- lists all cities in the database with their states name.
SELECT cities.id, cities.name, states.name
	FROM cities
	INNER JOIN states
	ON cities.state_id = states.id
	ORDER BY cities.id ASC;
