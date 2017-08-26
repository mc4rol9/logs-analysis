-- THE SQL VIEWS --

-- View for question 1 and 2--
CREATE VIEW top_articles AS
  SELECT title, 
  COUNT(log.id) AS pageviews
  FROM articles, log
    WHERE log.path = CONCAT('/article/', articles.slug)
  GROUP BY articles.title 
  ORDER BY pageviews desc;

-- View for question 2 --
CREATE VIEW top_authors AS
  SELECT title, name
  FROM articles, authors
    WHERE articles.author = authors.id;

-- Views for question 3 --
CREATE VIEW log_total AS
  SELECT date(time) as days, 
  CAST(count(status) AS FLOAT) AS status
  FROM log
  GROUP BY days
  ORDER BY days;

CREATE VIEW log_errors AS
  SELECT date(time) as days, 
  CAST(count(status) AS FLOAT) AS errors
  FROM log
    WHERE status!='200 OK'
  GROUP BY days
  ORDER BY days;

CREATE VIEW log_percentage AS
  SELECT log_errors.days, 
  (log_errors.errors*100)/log_total.status AS percentage
  FROM log_errors, log_total
    WHERE log_errors.days = log_total.days
  ORDER BY log_errors.days;