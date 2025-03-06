-- List all shows and their genre names
SELECT title, tv_genres.name AS gen_name FROM tv_shows
LEFT JOIN (
    tv_show_genres JOIN tv_genres
    ON tv_show_genres.genre_id = tv_genres.id
) ON tv_shows.id = tv_show_genres.show_id
ORDER BY title, gen_name;
