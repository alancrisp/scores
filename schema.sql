CREATE TABLE course (
    courseId int unsigned NOT NULL AUTO_INCREMENT,
    name varchar(100) NOT NULL,
    location varchar(30) NOT NULL,
    city varchar(30) NOT NULL,
    holes tinyint unsigned NOT NULL,
    PRIMARY KEY (courseId)
);

CREATE TABLE event (
    eventId int unsigned NOT NULL AUTO_INCREMENT,
    courseId int unsigned NOT NULL,
    eventDate date NOT NULL,
    PRIMARY KEY (eventId),
    CONSTRAINT FOREIGN KEY (courseId) REFERENCES course (courseId)
);

CREATE TABLE player (
    playerId int unsigned NOT NULL AUTO_INCREMENT,
    name varchar(30) NOT NULL,
    PRIMARY KEY (playerId)
);

CREATE TABLE score (
    scoreId int unsigned NOT NULL AUTO_INCREMENT,
    eventId int unsigned NOT NULL,
    playerId int unsigned NOT NULL,
    hole tinyint unsigned NOT NULL,
    score tinyint unsigned NOT NULL,
    PRIMARY KEY (scoreId),
    INDEX (eventId, playerId, hole),
    CONSTRAINT FOREIGN KEY (eventId) REFERENCES event (eventId),
    CONSTRAINT FOREIGN KEY (playerId) REFERENCES player (playerId)
);
