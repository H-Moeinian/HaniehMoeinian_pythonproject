import pandas as pd
import csv
import hashlib
from student import Student
from administrator import Administrator


class User:
    @staticmethod
    def register():
        student_or_administrator = input("are you a student or an administrator?\n"
                                         "1-student\n2-administrator\nyour choice: ")
        if student_or_administrator == '2':
            key = input("plaese enter the security key: ")
            if key != 'a1z9f4':
                print("wrong security key. you can not register as an administrator!")
                return
        df_account = pd.read_csv('login_info.csv')
        list_username = list(df_account['username'])
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
        row_account = [username, hashed_password]
        with open('login_info.csv', 'a', newline='') as csv_account:
            csv_writer = csv.writer(csv_account)
            csv_writer.writerow(row_account)
        if student_or_administrator == '1':
            with open('students.csv','a',newline='') as info_file:
                csv_writer = csv.writer(info_file)
                csv_writer.writerow([username, major, 0, ' '])


    @staticmethod
    def log_in():
        print("------------------------------------------")
        student_or_administrator = input("are you a student or an administrator?\n"
                                         "1-student\n2-administrator\nyour choice: ")
        print("------------------------------------------")
        flag = False
        counter = 0
        username = input("please enter your username: ")
        if student_or_administrator == '1':
            with open("students.csv",'r',newline='') as my_file:
                students_ = csv.reader(my_file)
                for i in students_:
                    if i[0] == username:
                        break
                else:
                    print("you are not a student!")
                    return
        if student_or_administrator == '2':
            with open("students.csv",'r',newline='') as my_file:
                students_ = csv.reader(my_file)
                for i in students_:
                    if i[0] == username:
                        print('you are a student.'
                              ' you can not log in as an administrator!')
                        return
        with open('login_info.csv', 'r', newline='') as login_file:
            csv_reader = csv.reader(login_file)
            for row in csv_reader:
                if username == row[0]:
                    with open('locked_users.txt','r') as locked_file:
                        for line in locked_file.readlines():
                            if username == line.strip():
                                print('your account is locked!')
                                return
                    password = row[1]
                    flag = True
                    break
            if flag is False:
                print('there is not such a user!')
            else:
                while True:
                    entered_password = input('please enter your password: ')
                    if hashlib.sha256(entered_password.encode('utf8')).hexdigest() == password:
                        print('-----------------welcome------------------')
                        if student_or_administrator == '1':
                            with open('students.csv','r') as students_info:
                                csv_reader = csv.reader(students_info)
                                for student in csv_reader:
                                    if student[0] == username:
                                        return Student(student[0], student[1],
                                                       student[2],student[3] )
                        elif student_or_administrator == '2':
                            return Administrator(username)
                    elif counter == 2:
                        print('your account is locked!')
                        with open('locked_users.txt','a') as locked_file:
                            locked_file.write(f'{username}\n')
                        break
                    else:
                        print('wrong password!')
                        counter += 1


###############
#change password
# def change_password(self):
# change = pd.read_csv('register.csv')
# location = 0
# old_password = input("Enter old password: ")
# new_password = input("Enter new password: ")
# hash_old_pass = hashlib.sha1(old_password.encode()).hexdigest()
# hash_new_pass = hashlib.sha1(new_password.encode()).hexdigest()
# with open('register.csv', 'r') as my_file:
# # csv_writer = csv.DictWriter(my_file,fieldnames=['name','password'])
# csv_reader = csv.DictReader(my_file)
# for row in csv_reader:
# if row['name'] == self.username and row['password'] == hash_old_pass:
# self.password = hash_new_pass
# print("Your password is changed.")
# change.loc[location,'password'] = hash_new_pass
# change.to_csv('register.csv',index=False)
# location += 1

