import sqlite3
import os

def create_database():
    if os.path.exists("students.db"):
        os.remove("students.db")

    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    return conn, cursor
def create_table(cursor):
    cursor.execute('''
        CREATE TABLE students (
            id INTEGER PRIMARY KEY,
            name VARCHAR NOT NULL,
            age INTEGER,
            email VARCHAR UNIQUE ,
            city VARCHAR
        )
    ''')
    cursor.execute('''
        CREATE TABLE courses (
            id INTEGER PRIMARY KEY,
            course_name VARCHAR NOT NULL,
            instructor TEXT,
            credits INTEGER
        )
    ''')

def insert_sample_data(cursor):
    students = [
        (1, 'Alice jones', 20, 'alice@example.com', 'New York'),
        (2, 'Bob Smith', 19, 'bob@example.com', 'Los Angeles'),
        (3, 'Charlie Brown', 21, 'charlie@example.com', 'Chicago'),
        (4, 'Diana Prince', 22, 'diana@example.com', 'Wonderland'),
        (5, 'Ethan Hunt', 23, 'ethan@example.com', 'New York')
    ]
    cursor.executemany('''INSERT INTO students (id, name, age, email, city) VALUES (?, ?, ?, ?, ? )''', students)

    courses = [
        (1, 'Mathematics', 'Dr. Alan Turing', 4),
        (2, 'Physics', 'Dr. Marie Curie', 3),
        (3, 'Chemistry', 'Dr. Dmitri Mendeleev', 4),
        (4, 'Biology', 'Dr. Charles Darwin', 3)
    ]
    cursor.executemany('''INSERT INTO courses (id, course_name, instructor, credits) VALUES (?, ?, ?, ?)''', courses)
    print("Sample data inserted successfully.")

def basic_sql_operations(cursor):
    # Select all students
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()
    for row in records:
        print(row)
    # Select Colums 
    cursor.execute("SELECT name, email FROM students")
    records = cursor.fetchall()
    print(records)
    # Where Clause
    print("Students from New York:")
    cursor.execute("SELECT * FROM students WHERE city = 'New York'")
    records = cursor.fetchall()
    for row in records:
        print(row)
    #WHERE with STRING
    cursor.execute("SELECT * FROM students WHERE name LIKE 'A%'")
    records = cursor.fetchall()
    print("Students with names starting with 'A':")
    for row in records:
        print(row)
    #Order By
    print("Students ordered by age:")
    cursor.execute("SELECT * FROM students ORDER BY age")
    records = cursor.fetchall()
    for row in records:
        print(row)

def sql_update_delete_insert_operations(cursor):
    #Insert
    cursor.execute("INSERT INTO students (id, name, age, email, city) VALUES (6, 'Frank Castle', 24, 'frank@example.com', 'New York')")
    print("Inserted new student.")
    #Update
    cursor.execute("UPDATE students SET age = 25 WHERE id = 6")
    print("Updated student age.")
    #Delete
    cursor.execute("DELETE FROM students WHERE id = 6")
    print("Deleted student.")

def aggregate_functions(cursor):
    # Count
    cursor.execute("SELECT COUNT(*) FROM students")
    result = cursor.fetchone()
    print(result)
    # Average
    cursor.execute("SELECT AVG(age) FROM students")
    result = cursor.fetchone()
    print(result)
    # Max - Min
    cursor.execute("SELECT MAX(age), MIN(age) FROM students")
    result = cursor.fetchone()
    print(result)
    #Group By
    cursor.execute("SELECT city, COUNT(*) FROM students GROUP BY city")
    results = cursor.fetchall()
    print(results)

def answers(cursor):
    #SINAV SORULARININ CEVAPLARIDIR BUNLARI TEKRAR ETMELİSİN HAFTADA BİR GÜN
    #1) Bütün kursların bilgilerini getirin
    cursor.execute("SELECT * FROM courses")
    print(cursor.fetchall())
    #Bütün kurs bilgilerini getirir
    #2) Sadece eğitmenlerin ismini ve ders ismi bilgilerini getirin
    cursor.execute("SELECT Course_name, instructor FROM courses")
    print(cursor.fetchall())
    #Sadece eğitmenlerin ismi ve ders ismi bilgilerini getirir
    #3) Sadece 21 yaşındaki öğrencileri getirin
    cursor.execute("SELECT * FROM students WHERE age = 21")
    print(cursor.fetchall())
    #Sadece 21 yaşındaki öğrencileri getirir
    #4) Sadece Chicago'da yaşayan öğrencileri getirin
    cursor.execute("SELECT * FROM students WHERE city = 'Chicago'")
    print(cursor.fetchall())
    #Sadece Chicago'da yaşayan öğrencileri getirir
    #5) Sadece 'Dr. Anderson' tarafından verilen dersleri getirin
    cursor.execute("SELECT * FROM courses WHERE instructor = 'Dr. Anderson'")
    print(cursor.fetchall())
    #Sadece 'Dr. Anderson' tarafından verilen dersleri getirir
    #6) Sadece ismi 'A' ile başlayan öğrencileri getirin
    cursor.execute("SELECT * FROM students WHERE name LIKE 'A%'")
    print(cursor.fetchall())
    #Sadece ismi 'A' ile başlayan öğrencileri getirir
    #7) Sadece 3 ve üzeri kredi olan dersleri getirin
    cursor.execute("SELECT * FROM courses WHERE credits >= 3")
    print(cursor.fetchall())
    #Sadece 3 ve üzeri kredi olan dersleri getirir
    #Detaylı
    #1) Öğrencileri alphabetic şekilde dizerek getirin
    cursor.execute("SELECT * FROM students ORDER BY name ASC")
    print(cursor.fetchall())
    #Öğrencileri alphabetic şekilde dizerek getirir
    #2) 20 yaşından büyük öğrencileri, ismine göre sıralayarak getirin
    cursor.execute("SELECT * FROM students WHERE age > 20 ORDER BY name ASC")
    print(cursor.fetchall())
    #20 yaşından büyük öğrencileri, ismine göre sıralayarak getirir
    #3) Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirin
    cursor.execute("SELECT * FROM students WHERE city IN ('New York', 'Chicago')")
    print(cursor.fetchall())
    #Sadece 'New York' veya 'Chicago' da yaşayan öğrencileri getirir
    #4) Sadece 'New York' ta yaşamayan öğrencileri getirin
    cursor.execute("SELECT * FROM students WHERE city != 'New York'")
    print(cursor.fetchall())
    #Sadece 'New York' ta yaşamayan öğrencileri getirir ve != bulunmayanları getirir
    #SINAV BİTMİŞTİR

def main():
    conn , cursor = create_database()
    try:
        create_table(cursor)
        conn.commit()
        insert_sample_data(cursor)
        basic_sql_operations(cursor)
        conn.commit()
        sql_update_delete_insert_operations(cursor)
        conn.commit()
        aggregate_functions(cursor)
        conn.commit()
        answers(cursor)
        conn.commit()
    except sqlite3.Error as e:
        print(e)
    finally:
        conn.close()
if __name__ == "__main__":
    main()

#Debeaver Üzerinden database e erişim sağlanabilir.
