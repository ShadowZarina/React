-- Select all people who starred in a movie with Kevin Bacon
SELECT people.name
FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.id IN
(
    -- Identify movies where Kevin Bacon starred
    SELECT movies.id
    FROM movies
    JOIN stars ON movies.id = stars.movie_id
    JOIN people ON stars.person_id = people.id
    WHERE people.name = 'Kevin Bacon' AND people.birth = 1958
)
-- Remove Kevin Bacon himself from results
AND people.name != 'Kevin Bacon';

