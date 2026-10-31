import sqlite3
import os


class Database:
    def __init__(self, data_dir):
        os.makedirs(data_dir, exist_ok=True)
        self.path = os.path.join(data_dir, "amie.db")
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "CREATE TABLE IF NOT EXISTS messages ("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "role TEXT NOT NULL, "
                "content TEXT NOT NULL)"
            )

    def add(self, role, text):
        with sqlite3.connect(self.path) as conn:
            conn.execute(
                "INSERT INTO messages (role, content) VALUES (?, ?)",
                (role, text)
            )

    def latest(self, n=20):
        with sqlite3.connect(self.path) as conn:
            rows = conn.execute(
                "SELECT role, content FROM messages ORDER BY id DESC LIMIT ?",
                (n,)
            ).fetchall()
        return list(reversed(rows))

    def clear(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("DELETE FROM messages")
