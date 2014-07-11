-- Problem - 1 - (a) select: Write a query that is equivalent to the following relational algebra expression.
select count(*) from frequency where docid="10398_txt_earn";

-- Problem - 1 - (b) select project: Write a SQL statement that is equivalent to the following relational algebra expression.
select count(*) from frequency where docid="10398_txt_earn" and count=1;

-- Problem - 1 - (c) union: Write a SQL statement that is equivalent to the following relational algebra expression. (Hint: you can use the UNION keyword in SQL)
select count(*) from (select term from frequency where docid="10398_txt_earn" and count=1 union select term from frequency where docid="925_txt_trade" and count=1);

-- Problem - 1 - (d) count: Write a SQL statement to count the number of documents containing the word "parliament"
select count(*) from frequency where term="parliament";

-- Problem - 1 - (e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. (Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
select count(*) from (select docid, sum(frequency.count) as occurences from frequency group by docid) where occurences > 300;

-- Problem - 1 - (f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
select count(*) from (select docid from frequency where term="transactions" intersect select docid from frequency where term="world");