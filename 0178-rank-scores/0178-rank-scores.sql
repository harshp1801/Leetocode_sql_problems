select round(score,2) score, dense_rank() over (order by score desc) as 'rank' from Scores

