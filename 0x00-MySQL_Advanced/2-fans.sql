--USE  hbtn_0d_tvshows;
--file contains sql script that  that ranks country origins of bands,
-- ordered by the number of (non-unique) fans
SELECT origin, SUM(fans) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;

