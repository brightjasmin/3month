CREATE_TABLE_TASK = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        is_completed BOOLEAN NOT NULL DEFAULT 0
    )
"""

INSERT_TASK = 'INSERT INTO tasks (task) VALUES (?)'

SELECT_TASK = "SELECT id, task FROM tasks"

UPDATE_TASK = "UPDATE tasks SET task = ? WHERE id = ?"

DELETE_TASK = 'DELETE FROM tasks WHERE id = ?'