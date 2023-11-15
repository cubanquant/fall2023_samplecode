import sqlite3


def create_tables():
    con = sqlite3.connect('pets.db')
    with con:
        cur = con.cursor()
        cur.execute("DROP TABLE IF EXISTS person;")
        cur.execute("CREATE TABLE person(id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER);")


if __name__ == "__main__":
    create_tables()
