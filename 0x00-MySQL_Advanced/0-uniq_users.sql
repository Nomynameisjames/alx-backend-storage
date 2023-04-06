/* SELECTS A DATABASE; */
--USE hbtn_0d_tvshows;
/*CHECKS IF TABLE EXISTS IF IT DOES DELETE */
--DROP TABLE IF EXISTS user;

CREATE TABLE users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255),
	PRIMARY KEY(`id`)
);

/* creates a new table on the selected database and sets id as the primary key
   ensure its not initialised with a default value of NULL
   also creates a column email with a UNIQUE INDEX syntax
*/
