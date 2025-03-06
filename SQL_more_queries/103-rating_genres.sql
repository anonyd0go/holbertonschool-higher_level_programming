-- Lists all genres in hbtn_0d_tvshows_rate by rating
SELECT name, SUM(tv_show_ratings.rate) AS rating FROM tv_genres
JOIN (
    tv_show_genres JOIN tv_show_ratings
    ON tv_show_genres.show_id = tv_show_ratings.show_id
) ON id = tv_show_genres.genre_id
GROUP BY name
ORDER BY rating DESC;
