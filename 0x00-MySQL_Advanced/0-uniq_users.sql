-- USE hbtn_0d_tvshows;
/* selects MYSQL database to utilize */

-- DROP TABLE IF EXISTS users;
/* checks the newly selected database if a users table exists if it does it deletes */

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
