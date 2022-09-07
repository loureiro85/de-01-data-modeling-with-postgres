# de-01-data-modeling-with-postgres
Data Modeling with Postgres - Udacity's Nanodegree Project


# Troubleshooting

Install postgresql

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