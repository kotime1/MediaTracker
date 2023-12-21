DROP TABLE IF EXISTS media
DROP TABLE IF EXISTS genre
DROP TABLE IF EXISTS language
DROP TABLE IF EXISTS status

DROP TABLE IF EXISTS media_genre
DROP TABLE IF EXISTS media_language
DROP TABLE IF EXISTS media_status


CREATE TABLE media (
    id PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(256),
    releaseYear int,
    rating decimal,
    int episodes,
    int completedEps
)

CREATE TABLE genre (
    id PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32)
)

CREATE TABLE language (
    id PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(32)
)

CREATE TABLE status(
    id PRIMARY KEY AUTO_INCREMENT,
    status VARCHAR(32)
)

CREATE TABLE media_language(
    mediaID FOREIGN KEY REFERENCES media(id)
    languageID FOREIGN KEY REFERENCES language(id)
)

CREATE TABLE media_genre(
    mediaID FOREIGN KEY REFERENCES media(id)
    genreID FOREIGN KEY REFERENCES genre(id)
)

CREATE TABLE media_status(
    mediaID FOREIGN KEY REFERENCES media(id)
    statusID FOREIGN KEY REFERENCES status(id)
)