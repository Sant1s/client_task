import sqlite3

def start():
    con = sqlite3.connect("prjct_db.db")
    cur = con.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Characters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS GeoData (
            id INTEGER PRIMARY KEY,
            character_id INTEGER,
            measurement_datetime TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            FOREIGN KEY (character_id) REFERENCES Characters(id)
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS Trajectories (
            id INTEGER PRIMARY KEY,
            character_id INTEGER,
            point_datetime TEXT NOT NULL,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            FOREIGN KEY (character_id) REFERENCES Characters(id)
        )
    ''')

    con.commit()
    con.close()


# Функция для добавления нового персонажа
def add_character(name):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Characters (name) VALUES ('{}')".format(name))
    conn.commit()
    conn.close()


# Функция для записи геоданных персонажа
def add_geo_data(character_id, measurement_datetime, latitude, longitude):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO GeoData (character_id, measurement_datetime, latitude, longitude) VALUES ('{}', '{}', '{}', '{}')".format(
            character_id, measurement_datetime, latitude, longitude))
    conn.commit()
    conn.close()


# Функция для записи точек траектории персонажа
def add_trajectory_point(character_id, point_datetime, latitude, longitude):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO Trajectories (character_id, point_datetime, latitude, longitude) VALUES ('{}', '{}', '{}', '{}')".format(
            character_id, point_datetime, latitude, longitude))
    conn.commit()
    conn.close()


# Функция для получения всех персонажей
def get_all_characters():
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Characters")
    rows = cursor.fetchall()
    conn.close()
    return rows


# Функция для получения всех геоданных персонажа
def get_character_geo_data(character_id):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM GeoData WHERE character_id={}".format(character_id))
    rows = cursor.fetchall()
    conn.close()
    return rows


# Функция для получения всех точек траектории персонажа
def get_character_trajectory(character_id):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Trajectories WHERE character_id={}".format(character_id))
    rows = cursor.fetchall()
    conn.close()
    return rows


def delete_character(character_id):
    conn = sqlite3.connect('prjct_db.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Characters WHERE id={}".format(character_id, ))
    cursor.execute("DELETE FROM GeoData WHERE character_id={}".format(character_id, ))
    cursor.execute("DELETE FROM Trajectories WHERE character_id={}".format(character_id, ))

    conn.commit()
    conn.close()


def get_character_id_by_name(name):
    conn = sqlite3.connect('prjct_db.db')
    cur = conn.cursor()
    cur.execute("SELECT id FROM Characters WHERE name='{}'".format(name))
    character_id = cur.fetchone()
    conn.commit()
    conn.close()
    return character_id[0] if character_id else None


def get_character_trajectory_points(character_id):
    conn = sqlite3.connect('prjct_db.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM Trajectories WHERE character_id={}".format(character_id, ))
    points = cur.fetchall()
    conn.commit()
    conn.close()
    return points


def get_all_characters_with_current_position():
    conn = sqlite3.connect('prjct_db.db')
    cur = conn.cursor()
    cur.execute(
        "SELECT c.id, c.name, t.latitude, t.longitude FROM Characters c JOIN Trajectories t ON c.id = t.character_id "
        "WHERE t.id IN (SELECT MAX(id) FROM Trajectories GROUP BY character_id)")
    characters = cur.fetchall()
    conn.commit()
    conn.close()
    return characters
