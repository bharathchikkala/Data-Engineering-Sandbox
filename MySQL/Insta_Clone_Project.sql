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
