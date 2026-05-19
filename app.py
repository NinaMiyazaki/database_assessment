

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
        # Prints results clearly
        print('TEACHER NAME   MAIN SUBJECT')
        for info in results:
            print(f'{info[0]: <15}{info[1]}')
       
# Main code
if __name__ == "__main__":
    choice = input(
    '''
    What would you like to do?
    1. Print all teacher information
    ''')
    if choice == '1':
        print_all_teacher_info()