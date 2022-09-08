# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"
logartist_table_drop = "DROP TABLE IF EXISTS logartists;"

# CREATE TABLES

        # songplay_id INT,
        # PRIMARY KEY (songplay_id)
songplay_table_create = ("""
    CREATE TABLE IF NOT EXISTS songplays (
        start_time timestamp,
        user_id INT,
        level VARCHAR,
        song_id VARCHAR,
        artist_id VARCHAR,
        session_id INT,
        location VARCHAR,
        user_agent VARCHAR
    );
""")

user_table_create = ("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INT,
        first_name VARCHAR,
        last_name VARCHAR,
        gender VARCHAR,
        level VARCHAR,
        PRIMARY KEY (user_id)
    );
""")

song_table_create = ("""
    CREATE TABLE IF NOT EXISTS songs (
        song_id VARCHAR,
        title VARCHAR,
        artist_id VARCHAR,
        year INT,
        duration DECIMAL,
        PRIMARY KEY (song_id)
    );
""")

artist_table_create = ("""
    CREATE TABLE IF NOT EXISTS artists (
        artist_id VARCHAR,
        artist_name VARCHAR,
        artist_location VARCHAR,
        artist_latitude DECIMAL,
        artist_longitude DECIMAL,
        PRIMARY KEY (artist_id)
    );
""")

time_table_create = ("""
    CREATE TABLE IF NOT EXISTS time (
        start_time timestamp,
        hour INT,
        day INT,
        week INT,
        month INT,
        year INT,
        weekday INT,
        PRIMARY KEY (start_time)
    );
""")

logartist_table_create = ("""
    CREATE TABLE IF NOT EXISTS logartists (
        artist_name VARCHAR,
        session_id INT,
        PRIMARY KEY (artist_name)
    );
""")

# INSERT RECORDS

        # songplay_id,
songplay_table_insert = ("""
    INSERT INTO songplays (
        start_time,
        user_id,
        level,
        song_id,
        artist_id,
        session_id,
        location,
        user_agent
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

user_table_insert = ("""
    INSERT INTO users (
        user_id,
        first_name,
        last_name,
        gender,
        level
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id) DO UPDATE
    SET first_name = EXCLUDED.first_name;
""")

song_table_insert = ("""
    INSERT INTO songs (
        song_id,
        title,
        artist_id,
        year,
        duration
    )
    VALUES (%s, %s, %s, %s, %s)
""")

artist_table_insert = ("""
    INSERT INTO artists (
        artist_id,
        artist_name,
        artist_location,
        artist_latitude,
        artist_longitude
    )
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO UPDATE
    SET artist_name = EXCLUDED.artist_name;
""")

time_table_insert = ("""
    INSERT INTO time (
        start_time,
        hour,
        day,
        week,
        month,
        year,
        weekday
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT DO NOTHING;
""")

# Debugging
logartist_table_insert = ("""
    INSERT INTO logartists (
        artist_name
    )
    VALUES (%s)
    ON CONFLICT (artist_name) DO NOTHING;
""")


# FIND SONGS
song_select = ("""
    SELECT song_id, songs.artist_id FROM songs
    JOIN artists ON songs.artist_id = artists.artist_id
    WHERE title=%s AND artist_name=%s AND duration=%s;
""")

# song_select = ("""
#     SELECT song_id, songs.artist_id FROM songs
#     JOIN artists ON songs.artist_id = artists.artist_id
#     WHERE title=%s AND artist_name=%s;
# """)

# QUERY LISTS

create_table_queries = [
    songplay_table_create,
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    logartist_table_create
]
drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop,
    logartist_table_drop
]
