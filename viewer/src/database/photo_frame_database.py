import sqlite3


class PhotoFrameDatabase:
    def __init__(self, database_path):
        self._database_path = database_path

    def _connect(self):
        return sqlite3.connect(self._database_path)

    def initialise(self):
        with self._connect() as connection:
            connection.execute(
                '''
                CREATE TABLE IF NOT EXISTS settings (
                name TEXT PRIMARY KEY,
                value TEXT NOT NULL
                )
                '''
                )

def set_setting(self, name, value):
    with self._connect() as connection:
        connection.execute(
            '''
            INSERT INTO settings (name, value)
            VALUES (?, ?)
            ON CONFLICT(name)
            DO UPDATE SET value = excluded.value
            ''',
            (name, value),
        )

def get_setting(self, name):
    with self._connect() as connection:
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

def get_wake_time(self):
    wake_time = (
    local_state.get_setting('wake_time')
    or DEFAULT_WAKE_TIME
)