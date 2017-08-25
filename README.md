# Logs Analysis Project
This is an internal reporting tool that uses information from the database to discover what kind of articles the site's readers like.

The given database contains newspaper articles, as well as the web server log for the site. 

This program was built in Python 3 and PostgreSQL and it runs from command line.
There is no user's input. The program connects to the database, uses SQL queries to analyze the log data, and print out the answers to some questions.

**_This is a project submission for Udacity Full Stack Web Developer Nanodegree Program._**

## Requirements
In order to run and make changes to this project, you'll need:
- [Python 3](https://www.python.org/)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads)
- [Vagrant](https://www.vagrantup.com/)
- [Udacity Vagrant config file](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)
- The newsdata.sql file from Udacity

## Usage
To run this project locally:

1. Download or clone this repository
2. Save the project folder inside Vagrant folder
3. Up and log into Vagrant VM
4. Load the *newsdata.sql* data into the local *news* database: `psql -d news`
5. Connect to the database: `psql -d news`
6. Create the VIEWS into the database - use the file *sql_views* as a guide
7. Run the program: `python3 reporting_tool.py`

## Files
Understanding the files:

__*pep8_test.jpg*__
The PEP8 style recommendations test.

__*results.jpg*__
The program results screen.

__*reporting_tool.py*__
The program.

__*sql_views.txt*__
The views guide.