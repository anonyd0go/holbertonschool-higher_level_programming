-- Lists all shows by their ratings
SELECT title, SUM(tv_show_ratings.rate) AS rating FROM tv_shows
JOIN tv_show_ratings ON id = tv_show_ratings.show_id
GROUP BY title
ORDER BY rating DESC;
