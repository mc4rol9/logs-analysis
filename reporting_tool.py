#!/usr/bin/env python3
#
# Internal Reporting Tool

import psycopg2

# Global for database name
DBNAME = "news"


def db_execute(query):
    """Connect to the database and execute the query. Return the result."""
    try:
        db = psycopg2.connect(database=DBNAME)
        c = db.cursor()
        c.execute(query)
        answer = c.fetchall()
        db.close()
        return answer
    except:
        print("<error message>")


def question_one():
    """Pass query to execution. Print out the result to question 1."""
    query = ("select * from top_articles limit 3")
    answer = db_execute(query)
    print("\n QUESTION 1: What are the most popular "\
          "three articles of all time?\n")
    print(" ANSWER:")
    print("\n  -- THE TOP 3 Popular Articles --\n")
    for count, (title, views) in enumerate(answer, 1):
        print(' {}. \"{}\" with {} views\n'.format(count, title, views))


def question_two():
    """Pass query to execution. Print out the result to question 2."""
    query = ("""SELECT name, SUM(top_articles.pageviews) AS views
                FROM top_authors, top_articles 
                WHERE top_authors.title = top_articles.title
                GROUP BY name
                ORDER BY views desc""")
    answer = db_execute(query)
    print("\n QUESTION 2: Who are the most popular "\
          "article authors of all time?\n")
    print(" ANSWER:")
    print("\n  -- MOST Popular Authors --\n")
    for count, (name, views) in enumerate(answer, 1):
        print(' {}. \"{}\" with {} views\n'.format(count, name, views))


def question_three():
    """Pass query to execution. Print out the result to question 3."""
    query = ("select * from log_percentage "
             "where percentage > 1.0 order by days")
    answer = db_execute(query)
    print("\n QUESTION 3: On which days did more than 1%"\
          "of requests lead to errors?\n")
    print(" ANSWER:")
    print("\n  -- DAYS/ERRORS LIST --\n")
    for count, (day, error) in enumerate(answer, 1):
        print(' {}. \"{}\" with a percentage of \"{:.2f}\" errors'.format(
              count, day, error))


if __name__ == '__main__':
    print("\n\n ////**** WELCOME TO THE REPORTING TOOL ****////\n")
    question_one()
    question_two()
    question_three()
    print("\n\n ////**** THANK YOU! ****////\n\n\n")
