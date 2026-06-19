CREATE DATABASE insta_clone;

USE insta_clone;

-- Users Schema
CREATE TABLE users(
	id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(200) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT NOW()
	);
    
DESC users;

-- Photos Schema
CREATE TABLE photos(
	id INT PRIMARY KEY AUTO_INCREMENT,
    image_url VARCHAR(200) NOT NULL,
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW()
    );
    
DESC photos;

-- Comments Schema
CREATE TABLE comments(
	id INT PRIMARY KEY AUTO_INCREMENT,
    comment_text VARCHAR(300),
    user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    photo_id INT NOT NULL,
    FOREIGN KEY(photo_id) REFERENCES photos(id),
    created_at TIMESTAMP DEFAULT NOW()
	);
    
DESC comments;

-- Likes Schema
CREATE TABLE likes(
	user_id INT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id),
    photo_id INT NOT NULL,
    FOREIGN KEY(photo_id) REFERENCES photos(id),
    created_at TIMESTAMP DEFAULT NOW(),
    PRIMARY KEY(user_id,photo_id)
);
-- DROP TABLE likes;
DESC likes;

-- Follows Schema
CREATE TABLE follow_people(
	follower_id INT NOT NULL,
    followee_id INT NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    FOREIGN KEY(follower_id) REFERENCES users(id),
	FOREIGN KEY(followee_id) REFERENCES users(id),
    PRIMARY KEY(follower_id,followee_id)
);

-- Tags
CREATE TABLE tags (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  tag_name VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
);
CREATE TABLE photo_tags (
    photo_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY(photo_id) REFERENCES photos(id),
    FOREIGN KEY(tag_id) REFERENCES tags(id),
    PRIMARY KEY(photo_id, tag_id)
);
show tables;
