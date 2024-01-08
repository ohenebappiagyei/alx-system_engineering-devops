-- Get the genre ID for Comedy
SELECT id FROM tv_genres WHERE name = 'Comedy';

-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE id NOT IN (
    -- Subquery to get the show IDs with the genre Comedy
    SELECT tv_show_genres.tv_show_id
    FROM tv_genres
    JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;

