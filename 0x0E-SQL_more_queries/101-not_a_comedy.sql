-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.

SELECT tv_shows.title 
FROM tv_shows
WHERE tv_shows.title NOT IN (
  SELECT tv_shows.title
  FROM tv_shows
  JOIN tv_show_genres AS tsg ON tsg.show_id = tv_shows.id 
  JOIN tv_genres AS tg ON tg.id = tsg.genre_id
  WHERE tg.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
