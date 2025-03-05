-- lists all cities from california that can be found in db
-- order by id
SELECT id, name FROM cities
WHERE state_id = (
    SELECT id FROM states
    WHERE name = "California"
)
ORDER BY id;
