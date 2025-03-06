-- Shows shows where genre id is NULL
SELECT title, tv_show_genres.genre_id
FROM tv_shows LEFT JOIN tv_show_genres ON id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY title;
