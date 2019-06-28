

userRequestIdWithName = 'SELECT id FROM user WHERE username = ?'
userRequestUserWithID = 'SELECT * FROM user WHERE id = ?'
userRequestUserWithName = 'SELECT * FROM user WHERE username = ?'
insertUser = 'INSERT INTO user (username, password) VALUES (?, ?)'
joinUserInfo = 'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id ORDER BY created DESC'
insertPost = 'INSERT INTO post (title, body, author_id) VALUES (?, ?, ?)'
fetchPost = 'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = u.id WHERE p.id = ?'
updatePost = 'UPDATE post SET title = ?, body = ? WHERE id = ?'
deletePost = 'DELETE FROM post WHERE id = ?'