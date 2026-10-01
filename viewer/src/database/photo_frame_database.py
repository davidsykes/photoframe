from contextlib import closing
from pathlib import Path
import sqlite3


class PhotoFrameDatabase:
    def __init__(self, database_path):
        self._database_path = Path(database_path)

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def initialise(self):
        with closing(self._connect()) as connection:
            connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS settings (
                name TEXT PRIMARY KEY,
                value TEXT NOT NULL
                )
                '''
                )
            connection.commit()

    def set_setting(self, name, value):
        with closing(self._connect()) as connection:
            connection.execute(
                '''
                INSERT INTO settings (name, value)
                VALUES (?, ?)
                ON CONFLICT(name)
                DO UPDATE SET value = excluded.value
                ''',
                (name, value),
            )
            connection.commit()

    def get_setting(self, name):
        with closing(self._connect()) as connection:
            row = connection.execute(
                '''
                SELECT value
                FROM settings
                WHERE name = ?
                ''',
                (name,),
            ).fetchone()

        if row is None:
            return None

        return row[0]
