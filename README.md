# Logs Analysis Project
This is an internal reporting tool that uses information from the database to discover what kind of articles the site's readers like.

The given database contains newspaper articles, as well as the web server log for the site. 

This program was built in Python3 and PostgreSQL and it runs from command line.
There is no user's input. The program connects to the database, uses SQL queries to analyze the log data, and print out the answers to questions:

1. What are the most popular three articles of all time? 
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

**_This is a project submission for Udacity Full Stack Web Developer Nanodegree Program._**

## Requirements
In order to run and make changes to this project, you'll need:
- [Python 3](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)

Projects files and Modules: 
- Download the data sample for this project 
  - [newsdata.sql file from Udacity](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
- Download or clone this project repository
- Install the *psycopg2* module: `pip3 install psycopg2`

## Usage
Make sure to save the data sample file *newsdata.sql* inside project directory.

**Build the database**
1. Load the data to a local *news* database: `psql -d news -f newsdata.sql`
2. Create the VIEWS into the database:'`psql -d news -f sql_views.sql`
3. Connect to the local database: `psql -d news`

**Run the program**
`python3 reporting_tool.py`

## Files
Understanding the files:

__*reporting_tool.py*__
The program.

__*results.jpg*__
The program results screen.

__*sql_views.sql*__
The file to create the VIEWS.