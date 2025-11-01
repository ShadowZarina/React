-- Select all Harry Potter movies and arrange them in chronological order 
SELECT title, year
FROM movies
WHERE title LIKE "Harry Potter%"
ORDER BY year ASC;
