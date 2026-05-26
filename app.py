

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
        print('TEACHER NAME:  MAIN SUBJECT:')
        for info in results:
            print(f'{info[0]: <15}{info[1]}') # could print it in alphabetical order?

def print_teachers_by_subject():
    for number, subject in subjects.items():
        print(f'{number}. {subject}')
        try: 
            choice = int(input('Select a subject by entering the corresponding number: '))
            if choice in subjects:
                with sqlite3.connect(DATABASE) as db:
                    cursor = db.cursor()
                    sql = "SELECT teacher_name FROM teacher WHERE main_subject = ? ORDER BY teacher_name;" 
                    cursor.execute(sql, (subjects[choice],))
                    results = cursor.fetchall()
                    print(f'Teachers who teach {subjects[choice]}:')
                    for teacher in results:
                        print(teacher[0])
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a number.')

def comment_on_teacher():
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        sql = "SELECT id, teacher_name FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        for id, teacher in results:
            print(f'{id}. {teacher}') 
        try:
            choice = int(input('Select a teacher by entering the corresponding number: '))
            if 1 <= choice <= len(results):
                selected_teacher = results[choice - 1]
                teacher_id = selected_teacher[0]
                teacher_name = selected_teacher[1]
                comment = input(f'Enter your comment for {teacher_name} (include date and period if relevant): ')
                sql = "INSERT INTO feedback (teacher_id, comment) VALUES (?, ?);"
                cursor.execute(sql, (teacher_id, comment))
                db.commit()
                print('Comment added successfully.')
            else:
                print('Please enter a valid number.')
        except ValueError:
            print('Please enter a number.')

# Main code
if __name__ == "__main__":
    while True:
        # Asks user what they want to do
        choice = input(
        '''
        What would you like to do?
        1. Print all teacher information
        2. Print teachers by subject
        3. Comment on a teacher
        4. Print teacher feedback
        5. Exit
        Select a number: ''') # sort out that it prints this in the middle of the terminal 
        # remember to add an exit option and ask for them to enter a number 
        # 
        if choice == '1':
                print_all_teacher_info()
        elif choice == '2':
            print_teachers_by_subject()
        elif choice == '3':
            comment_on_teacher()
        elif choice == '4':

        elif choice == '5':
            break
        else: 
            print('Please enter a valid number.')

# rememeber to test inputs by inputting enter