-- Select titles of all movies with release dates on/after 2018 in alphabetical order
SELECT title
FROM movies
WHERE year >= 2018
ORDER BY title ASC;
