

# Imports
import sqlite3

# Constants
DATABASE = 'teacher_feedback.db'

# Functions
def print_all_teacher_info():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT teacher_name, main_subject FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        #
        print(results)



