import sqlite3
from db import queries
from config import path_db

def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_TABLE_TASK)
    print("База данных подключена!")
    conn.commit()
    conn.close()

def mark_task_as_completed(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET is_completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()



def delete_completed_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE is_completed = 1")
    conn.commit()
    conn.close()


def add_task(task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_TASK, (task, ))
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def get_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.SELECT_TASK)
    tasks = cursor.fetchall()
    conn.close()
    return tasks


def delete_task(task_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_TASK, (task_id, ))
    conn.commit()
    conn.close()

def delete_all_tasks():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()


def update_task(task_id, new_task):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(queries.UPDATE_TASK, (new_task, task_id))
    conn.commit()
    conn.close()