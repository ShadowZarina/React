-- Select he names of all songs where danceability, energy, and valence are all greater than 0.75
SELECT name
FROM songs
WHERE danceability > 0.75 AND energy > 0.75 AND valence > 0.75;
