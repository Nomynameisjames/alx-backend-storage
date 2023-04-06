--USE hbtn_0d_tvshows
/* create a table users checks if it already exists and creates it if doesn't */

CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL AUTO_INCREMENT,
    	email VARCHAR(255) NOT NULL UNIQUE,
    	name VARCHAR(255),
    	country ENUM('CO', 'US', 'TN') NOT NULL DEFAULT 'US',
	PRIMARY KEY(id)
);

/* One of the distinct datatype used in this file
   is the ENUM in the country column which enables it
   to have a set likely value of occurance,
   sets the default country to US and ensure one of
   either values set is used in the  column 

*/
