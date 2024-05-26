import sqlite3

try:
    # Create/connect to database
    db = sqlite3.connect('file/python_programming_database.db')

    # Create cursor to execute SQL statements
    cursor = db.cursor()

    # Create table python_programming and insert columns
    cursor.execute('''CREATE TABLE IF NOT EXISTS python_programming (
                id INTEGER PRIMARY KEY, name TEXT, grade INTEGER)''')

    # Insert records from tuples list
    student_grades = [
                    (55, 'Carl Davis', 61),
                    (66, 'Dennis Fredrickson', 88),
                    (77, 'Jane Richards', 78),
                    (12, 'Peyton Sawyer', 45),
                    (2, 'Lucas Brooke', 99)
                    ]

    cursor.executemany('''INSERT OR IGNORE INTO python_programming (id, name, grade)
                          VALUES (?, ?, ?)''', student_grades)

    # Query 1: Select all records with a grade between 60 and 80.
    cursor.execute('''SELECT * FROM python_programming
                      WHERE grade > 60 AND grade < 80''')
    print(cursor.fetchall())

    # Query 2: Change Carl Davis’s grade to 65.
    new_grade = 65
    id = 55
    cursor.execute('''UPDATE python_programming SET grade = ?
                      WHERE id = ?''', (new_grade, id))

    # Query 3: Delete Dennis Fredrickson’s row.
    id = 66
    cursor.execute('''DELETE FROM python_programming WHERE id = ?''', (id,))

    # Query 4: Change the grade of all students with 
    # an id greater than 55 to a grade of 80.
    new_grade = 80
    cursor.execute('''UPDATE python_programming SET grade = ?
                      WHERE id > 55''', (new_grade,))

    # Commit changes
    db.commit()

except Exception as e:
    db.rollback()
    raise e

finally:
    db.close()
