-- list number of records with the same score
SELECT score, COUNT(score) FROM second_table GROUP BY score;