

# Imports
import sqlite3

# Constants and variables
DATABASE = 'teacher_feedback.db'
subjects = {
    1: 'English',
    2: 'Mathematics',
    3: 'Science',
    4: 'Technology',
    5: 'Drama',
    6: 'Japanese'
}

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

def print_teachers_by_subject():
    for number, subject in subjects.items():
        print(f'{number}. {subject}')
        try: 
            choice = int(input('Select a subject by entering the corresponding number: '))
            if choice in subjects:
                with sqlite3.connect(DATABASE) as db:
                    cursor = db.cursor()
                    sql = "SELECT teacher_name FROM teacher WHERE main_subject = ?;" # order the names alphabetically
                    cursor.execute(sql, (subjects[choice],))
                    results = cursor.fetchall()
                    print(f'Teachers who teach {subjects[choice]}:') # maybe change this sentence
                    for teacher in results:
                        print(teacher[0])
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a number.')


            
    
 

        sql = "SELECT teacher_name, main_subject FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # Prints results clearly
        print('TEACHER NAME   MAIN SUBJECT')
        for info in results:
            print(f'{info[0]: <15}{info[1]}')


# Main code
if __name__ == "__main__":
    while True:
        # Asks user what they want to do
        choice = input(
        '''
        What would you like to do?
        1. Print all teacher information
        Select a number: ''')
        # remember to add an exit option and ask for them to enter a number 
        # 
        if choice == '1':
                print_all_teacher_info()
        else: 
            print('Please enter a valid number.')