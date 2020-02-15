import sqlite3


class Database:

    def __init__(self, db):
        self.connection = sqlite3.connect(db)
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, author text, note text, date text)")
        self.connection.commit()

    def fetch(self):
        self.cursor.execute("SELECT * FROM notes")
        rows = self.cursor.fetchall()
        return rows

    def insert(self, author, note, date):
        bla = 1
        self.cursor.execute("INSERT INTO notes(author, note, date) VALUES (?, ?, ?)", (author, note, date))
        self.connection.commit()

    def remove(self, note_id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.connection.commit()

    def update(self, note_id, author, note, date):
        self.cursor.execute("UPDATE notes SET author = ?, note = ?, date = ? WHERE id = ?",
                            (author, note, date, note_id))
        self.connection.commit()

    def __del__(self):
        self.connection.close()
