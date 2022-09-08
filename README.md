# de-01-data-modeling-with-postgres
Data Modeling with Postgres - Udacity's Nanodegree Project


# Document Process


## 1. Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.
This database provides tables for data analytics.
The following tables were created:
- Songplays (fact)
- Users (dimension)
- Songs (dimension)
- Artists (dimension)
- Time (dimension)

This schema directly suggests 4 analysis, by User, by Songs, by Artists, by Time.
The following questions indicate possible reports/dashboards:
- Time: What is the day of the week that people most listen to music?
- Users: What age group mostly uses the song app?
- Artists: Who is the artist with the highest playback count?
- Song: What are the top 10 songs of all times?

This database may serve Data Analysts and Data Scientists, for reports, dashboards, machine learning models, etc.

## 2. How to run the Python scripts
Two Python scripts must run:
1. `create_tables.py`
2. `etl.py`

In my implementation, these scripts run inside a virtual environment with the packages listed in `requirements.txt`.
Also, postgresql must be installed, and access must be granted to create databases. More details in the Troubleshooting section, at the end of this readme.

## 3. An explanation of the files in the repository
These are the most relevant files (based on Udacity's Project Instructions):
- `test.ipynb` displays the first few rows of each table to let you check your database. Checks for the implementation of primary keys and not null constraints during table's creation.
- `create_tables.py` drops and creates your tables. You run this file to reset your tables before each time you run your ETL scripts. Also creates/recreates database and returns cursor and connector.
- `etl.ipynb` reads and processes a single file from song_data and log_data and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables. This notebook is suitable for data exploration and ETL development.
- `etl.py` reads and processes files from song_data and log_data and loads them into your tables. You can fill this out based on your work in the ETL notebook. This script is suitable for production.
- `sql_queries.py` contains all your sql queries, and is imported into the last three files above.
- `requirements.txt` contains all python packages required.
- `tox.ini` contains Flake8 linting instructions, such as the maximum line length set to 100 characters.




## 4. State and justify your database schema design and ETL pipeline.
**Database schema**
The database schema is based on the Fact-Dimension approach.
Facts are related to events when a song was played (start_time), whose artist it was (artist_id), who listened to it (user_id), what song (song_id), etc.
Hence, the dimensions are: users, songs, artists, and time.

This schema is justified by the intended use of the tables, for analytical purposes. It's fair to imagine that Data Analysts and Data Scientists may extract and deliver value from it.

**ETL pipeline**
The ETL pipeline consists of:
- **Extracting** data from two kinds of JSON files. The first related to 'songs' and the second related to 'logs' that describe the events when the songs were played;
- **Transforming** data by filtering pages that are equal to 'NextSong', selecting columns, etc;
- **Loading** data in fact-dimension tables.


# Troubleshooting

## Install postgresql

https://www.shubhamdipt.com/blog/create-user-and-database-in-postgresql/

```
$ sudo su postgres
$ psql
postgres=#SHOW SERVER_ENCODING; # It should be UTF8
postgres=#CREATE USER myusername WITH ENCRYPTED PASSWORD 'mypassword';
postgres=#CREATE DATABASE mydatabase;
postgres=#GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myusername;

# If certain privileges are to be granted
# First USAGE on schema
postgres=#GRANT USAGE ON SCHEMA myschema TO myusername;
# Now specific privileges
postgres=#GRANT SELECT ON ALL TABLES IN SCHEMA myschema TO myusername;
```

## From udacity:
`alter user student createdb;`


`!pip install ipython-sql`

