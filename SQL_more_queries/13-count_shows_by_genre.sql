-- Shows genres and number of showls linked to each
SELECT name AS genre, COUNT(*) AS number_of_shows
FROM tv_genres JOIN tv_show_genres
ON id = tv_show_genres.genre_id
GROUP BY name
ORDER BY number_of_shows DESC;
