import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(empId, name, resumeFile):
    try:
        sqliteConnection = sqlite3.connect('ms.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO cbse
                                  (id, name, resume) VALUES (?, ?, ?)"""

        resume = convertToBinaryData(resumeFile)
        # Convert data into tuple format
        data_tuple = (empId, name, resume)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

#insertBLOB(1, "Smith", "C:/Users/Ajith P/PycharmProjects/pythonProject/edit1.txt")
#insertBLOB(3, "David", "C:/Users/Ajith P/PycharmProjects/pythonProject3/10thmaths.txt")

insertBLOB(3, "10th_class-English", "C:/Users/Ajith P/PycharmProjects/pythonProject7/10th-English.txt")
insertBLOB(4, "10th_class-Maths", "C:/Users/Ajith P/PycharmProjects/pythonProject7/10th-Maths.txt")
insertBLOB(5, "10th_class-Science", "C:/Users/Ajith P/PycharmProjects/pythonProject7/10th-Science.txt")
insertBLOB(6, "10th_class-Socialscience", "C:/Users/Ajith P/PycharmProjects/pythonProject7/10th-Socialscience.txt")
insertBLOB(7, "11th_class-Accountancy", "C:/Users/Ajith P/PycharmProjects/pythonProject7/11th-Accountancy.txt")
insertBLOB(8, "11th_class-Biology", "C:/Users/Ajith P/PycharmProjects/pythonProject7/11th-Biology.txt")
insertBLOB(9, "11th_class-Computerscience", "C:/Users/Ajith P/PycharmProjects/pythonProject7/11th-Computerscience.txt")
insertBLOB(10, "11th_class-Economics", "C:/Users/Ajith P/PycharmProjects/pythonProject7/11th-Economics.txt")
insertBLOB(11, "11th_class-Maths", "C:/Users/Ajith P/PycharmProjects/pythonProject7/11th-Maths.txt")
insertBLOB(12, "12th_class-Accountancy_1", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Accountancy_1.txt")
insertBLOB(13, "12th_class-Accountancy_2", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Accountancy_2.txt")
insertBLOB(14, "12th_class-Maths_1", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Maths_1.txt")
insertBLOB(15, "12th_class-Maths_2", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Maths_2.txt")
insertBLOB(16, "12th_class-Economics_1", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Economics_1.txt")
insertBLOB(17, "12th_class-Economics_2", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Economics_2.txt")
insertBLOB(18, "12th_class-Biology", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Biology.txt")
insertBLOB(19, "12th_class-Computerscience", "C:/Users/Ajith P/PycharmProjects/pythonProject7/12th-Computerscience.txt")