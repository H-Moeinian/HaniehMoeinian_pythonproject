import pandas as pd
import csv
import hashlib
from student import Student
from administrator import Administrator


class User:
    @staticmethod
    def register():
        status = {'1': 'student', '2': 'administrator'}
        student_or_administrator = input("are you a student or an administrator?\n"
                                         "1-student\n2-administrator\nyour choice: ")
        if student_or_administrator == '2':
            key = input("please enter the security key: ")
            if key != 'a1z9f4':
                print("wrong security key. you can not register as an administrator!")
                return
        try:
            df_account = pd.read_csv('login_info.csv')
            list_username = list(df_account['username'])
        except OSError as err:
            print(f"OS error: {err}")
        print("------------------------------------------")
        while True:
            username = input('please enter username: ')
            if username in list_username:
                print('username exists!')
            else:
                break
        password = input('please enter password: ')
        hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
        if student_or_administrator == '1':
            major = input("please enter your major: ")
        row_account = [username, hashed_password,status[student_or_administrator]]
        with open('login_info.csv', 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            csv_writer.writerow(row_account)

        if student_or_administrator == '1':
            with open('students.csv', 'a', newline='') as info_file:
                csv_writer = csv.writer(info_file)
                csv_writer.writerow([username, major, 0, ' '])

    @staticmethod
    def log_in():
        username = input("please enter your username: ")
        with open('login_info.csv') as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row[0] == username:
                    with open('locked_users.txt', 'r') as locked_file:
                        for line in locked_file.readlines():
                            if username == line.strip():
                                print('your account is locked!')
                                return
                    password = row[1]
                    status = row[2]
                    break
            else:
                print("there is not such a user!")
                return
        counter = 0
        while True:
            entered_password = input('please enter your password: ')
            if hashlib.sha256(entered_password.encode('utf8')).hexdigest() == password:
                print('-----------------welcome------------------')
                if status == 'student':
                    with open('students.csv', 'r') as students_info:
                        csv_reader = csv.reader(students_info)
                        for student in csv_reader:
                            if student[0] == username:
                                return Student(student[0], student[1],
                                               student[2], student[3])
                elif status == 'administrator':
                    return Administrator(username)
            elif counter == 2:
                print('your account is locked!')
                with open('locked_users.txt', 'a') as locked_file:
                    locked_file.write(f'{username}\n')
                break
            else:
                print('wrong password!')
                counter += 1


