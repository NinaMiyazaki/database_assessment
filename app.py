# Docstring - Nina Miyazaki - Teacher Feedback Database Application

# Imports
import sqlite3

# Constants and variables
# Database file name
DATABASE = 'teacher_feedback.db'
# The smallest number an id can be in this database
minimum_id = 1
# Number used to see if all password attempts are gone
no_attempts_left = 0
# Dictionary storing a number and subject 
subjects = {
    1: 'English',
    2: 'Mathematics',
    3: 'Science',
    4: 'Technology',
    5: 'Drama',
    6: 'Japanese'
}
# Dictionary storing teacher ids and their passwords
passwords = {
    1: 'unicorn123',
    2: 'griffin789',
    3: 'troll6767',
    4: 'dragon504',
    5: 'phoenix371',
    6: 'hydra362'
}

# Functions
# Displays all teacher data for user
def print_all_teacher_info():
    # Connects to the database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # Gets all teacher names and subjects
        sql = "SELECT teacher_name, main_subject FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # Prints results clearly
        print('TEACHER NAME:  MAIN SUBJECT:')
        for info in results:
            print(f'{info[0]: <15}{info[1]}')

# Displays teachers based on subject selected by user
def print_teachers_by_subject():
    # Displays subjects dictionary nicely
    for number, subject in subjects.items():
        print(f'{number}. {subject}')
    # Asks user to select a subject until input is valid
    while True:
        try:
            choice = int(input('Select a subject by entering the corresponding number: '))
        except ValueError:
            print('Please enter a number.')
            continue
        if choice in subjects:
            break
        else:
            print('Please enter a valid number.')
    # Connects to the database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # Gets all teachers that teach the subject user selected
        sql = "SELECT teacher_name FROM teacher WHERE main_subject = ? ORDER BY teacher_name;"
        cursor.execute(sql, (subjects[choice],))
        results = cursor.fetchall()
        # Displays results nicely 
        print(f'TEACHERS WHO TEACH {subjects[choice].upper()}:')
        for teacher in results:
            print(teacher[0])

# Allows user to comment on a teacher
def comment_on_teacher():
    # Connects to the database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # Retrieves all teacher ids and names
        sql = "SELECT id, teacher_name FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # Displays the results nicely 
        for id, teacher in results:
            print(f'{id}. {teacher}')
        # Asks user to select a number until input corresponds with a teacher
        while True:
            try:
                choice = int(input('Select a teacher by entering the corresponding number: '))
            except ValueError:
                print('Please enter a number.')
                continue
            if minimum_id <= choice <= len(results):
                break
            else:
                print('Please enter a valid number.')
        # Teacher id and name of selected teacher are saved to variables 
        selected_teacher = results[choice - 1]
        teacher_id = selected_teacher[0]
        teacher_name = selected_teacher[1]
        # Asks user for a comment until one is inputted 
        while True:
            comment = input(f'Enter your comment for {teacher_name} (include date and period if relevant): ').strip()
            if not comment:
                print("Comment cannot be empty. Please try again.")
            else:
                break
        # Adds comment to database
        sql = "INSERT INTO feedback (teacher_id, comment) VALUES (?, ?);"
        cursor.execute(sql, (teacher_id, comment))
        db.commit()
        # Tells user comment has been added
        print('Comment added successfully.')

# Allows a teacher to log in and view their feedback
def print_teacher_feedback():
    # Number of password attempts left
    attempts = 3
    # Connects to the database
    with sqlite3.connect(DATABASE) as db:
        cursor = db.cursor()
        # Gets all teacher ids and names
        sql = "SELECT id, teacher_name FROM teacher;"
        cursor.execute(sql)
        results = cursor.fetchall()
        # Displays all teacher ids and names
        for id, teacher in results:
            print(f'{id}. {teacher}')
        # Asks user which teacher they are until valid number is entered
        while True:
            try:
                choice = int(input('Select your name by entering the corresponding number: '))
            except ValueError:
                print('Please enter a number.')
                continue
            if minimum_id <= choice <= len(results):
                break
            else:
                print('Please enter a valid number.')
        # Loop runs until password is correct or attempts run out
        while attempts > no_attempts_left:
            password = input('Enter password: ')
            if passwords.get(choice) == password:
                print('Correct password.')
                break
            else:
                print('Incorrect password.')
            attempts -= 1
            if attempts == no_attempts_left:
                print('Too many incorrect attempts.')
                return
        # Gets all comments for the selected teacher
        sql = "SELECT comment FROM feedback WHERE teacher_id = ?;"
        cursor.execute(sql, (choice,))
        results = cursor.fetchall()
        # Displays comments if any
        if results:
            print('Your comments:')
            for comment in results:
                print(f'- {comment[0]}')
        else:
            print('No comments found')

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
Select a number: ''')
        # Runs the function the user input corresponds to
        if choice == '1':
            print_all_teacher_info()
        elif choice == '2':
            print_teachers_by_subject()
        elif choice == '3':
            comment_on_teacher()
        elif choice == '4':
            print_teacher_feedback()
        elif choice == '5':
            break
        else:
            print('Please enter a valid number.')

# if i had extra time i probably would have added the passwords to the database to minimize error