-- Select the names of songs that are by Post Malone
SELECT name
FROM songs
WHERE artist_id =
(
    -- Select the id that corresponds to Post Malone
    SELECT id
    FROM artists
    WHERE name = 'Post Malone'
);
