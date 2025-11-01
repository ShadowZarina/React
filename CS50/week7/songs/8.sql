-- Select the names of songs that feature other artists using "feat."
SELECT name
FROM songs
WHERE name LIKE '%feat.%';
