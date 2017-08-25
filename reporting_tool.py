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
        print("\nSorry, unable to connect to the database: " + DBNAME)


def question_one():
    """Pass query to execution. Print out the result to question 1."""
    query = ("select * from top_articles limit 3")
    answer = db_execute(query)
    print("\n QUESTION 1: What are the most popular "\
          "three articles of all time?\n")
    print(" ANSWER:")
    print("\n  -- THE TOP 3 Popular Articles --\n")
    count = 1
    for a in answer:
        print(" ", count, a[0], " with", a[1], "views\n")
        count = count + 1


def question_two():
    """Pass query to execution. Print out the result to question 2."""
    query = ("select name, sum(top_articles.pageviews) as views "
             "from top_authors, top_articles group by name "
             "order by views desc")
    answer = db_execute(query)
    print("\n QUESTION 2: Who are the most popular "\
          "article authors of all time?\n")
    print(" ANSWER:")
    print("\n  -- MOST Popular Authors --\n")
    count = 1
    for a in answer:
        print(" ", count, a[0], " with", a[1], "views\n")
        count = count + 1


def question_three():
    """Pass query to execution. Print out the result to question 3."""
    query = ("select * from log_percentage "
             "where percentage > 1.0 order by days")
    answer = db_execute(query)
    print("\n QUESTION 3: On which days did more than 1%"\
          "of requests lead to errors?\n")
    print(" ANSWER:")
    print("\n  -- DAYS/ERRORS LIST --\n")
    count = 1
    for a in answer:
        print(" ", count, a[0], "with a percentage of", ("%.2f" % a[1]),\
              "errors\n")
        count = count + 1


if __name__ == '__main__':
    print("\n\n ////**** WELCOME TO THE REPORTING TOOL ****////\n")
    question_one()
    question_two()
    question_three()
    print("\n\n ////**** THANK YOU! ****////\n\n\n")
