SELECT DISTINCT Views.author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY author_id