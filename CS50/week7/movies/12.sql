-- Identify movies that starred Bradley Cooper and Jennifer Lawrence at the same time
SELECT title
FROM movies
WHERE id IN (
    SELECT movie_id
    FROM stars
    WHERE person_id =
    (
        SELECT id
        FROM people
        WHERE name = 'Bradley Cooper'
    )
) -- Identify movies that also starred Jennifer Lawrence
AND id IN (
    SELECT movie_id
    FROM stars
    WHERE person_id =
    (
        SELECT id
        FROM people
        WHERE name = 'Jennifer Lawrence'
    )
);
