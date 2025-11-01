-- Select the names of people with corresponding person_ids
SELECT name
FROM people
WHERE id IN
(
    -- Select the person_id that corresponds to movie_id of Toy Story
    SELECT person_id
    FROM stars
    WHERE movie_id =
    (
        -- Select the movie id that corresponds to Toy Story
        SELECT id
        FROM movies
        WHERE title = 'Toy Story'
    )
);
