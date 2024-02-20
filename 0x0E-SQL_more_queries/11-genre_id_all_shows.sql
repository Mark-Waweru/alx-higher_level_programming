-- lists all shows contained in the database even if it doesn't have a genre
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_show_genres
	RIGHT JOIN tv_shows
	ON tv_show_genres.show_id = tv_shows.id
	ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
