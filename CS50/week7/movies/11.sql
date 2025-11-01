-- Select titles of five highest rated movies that starred Chadwick Boseman (in descending order of ratings)
SELECT movies.title
FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE people.name = 'Chadwick Boseman'
LIMIT 5
