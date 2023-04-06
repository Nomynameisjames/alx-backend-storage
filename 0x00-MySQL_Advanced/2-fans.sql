--USE  hbtn_0d_tvshows;
/* file contains sql script that  that ranks country origins of bands,
   ordered by the number of (non-unique) fans */

/* Delimiter is created to prevent the default use of the semi colon which 
  causes problem in stored procedure because a procedure can have many statements
*/
DROP PROCEDURE IF EXISTS fan_ranking;
DELIMITER $$
CREATE PROCEDURE fan_ranking()
    	BEGIN
		SELECT origin, SUM(fans) AS nb_fans
    		FROM metal_bands
    		GROUP BY origin
    		ORDER BY nb_fans DESC;
    	END$$
CALL fan_ranking()$$
DELIMITER ;$$

