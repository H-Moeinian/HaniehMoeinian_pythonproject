# import csv
#
#
# def register():
#     while True:
#         username = input('please enter a username: ')
#         flag = False
#         with open('login_info.csv', 'r', newline='') as login_file:
#             csv_reader = csv.DictReader(login_file)
#             for row in csv_reader:
#                 if username in row['username']:
#                     flag = True
#                     print("there is already someone with this username!")
#                     break
#         if flag == False:
#             while True:
#                 password = input('please enter a password with more than 4 characters: ')
#                 if len(password) <= 4:
#                     print('too short password!')
#                 else:
#                     break
#
#             with open('login_info.csv', 'a', newline='') as login_file:
#                 csv_writer = csv.DictWriter(login_file, fieldnames=['username', 'password'])
#                 csv_writer.writerow({'username': username, 'password': password})
#                 print("congratulations! you registered successfully.")
#                 break
#
#
# def log_in():
#     flag = False
#     counter = 0
#     username = input("please enter your username: ")
#     with open('login_info.csv', 'r', newline='') as login_file:
#         csv_reader = csv.reader(login_file)
#         for row in csv_reader:
#             if username == row[0]:
#                 with open('locked_users.txt','r') as locked_file:
#                     for line in locked_file.readlines():
#                         if username == line.strip():
#                             print('your account is locked!')
#                             return
#                 password = row[1]
#                 flag = True
#                 break
#         if flag is False:
#             print('there is not such a user!')
#         else:
#             while True:
#                 entered_password = input('please enter your password: ')
#                 if entered_password == password:
#                     print('welcome')
#                     return {'username': username, 'password': password}
#                 elif counter == 2:
#                     print('your account is locked!')
#                     with open('locked_users.txt','a') as locked_file:
#                         locked_file.write(f'{username}\n')
#                     break
#                 else:
#                     print('wrong password!')
#                     counter += 1
#
# while True:
#     action = input('what do you want to do? 1-register 2-login : ')
#     if action == '1':
#         register()
#     elif action == '2':
#         log_in()
#     else:
#         print('wrong input')


##################################
##register implementation by teacher
# import pandas as pd
# import hashlib
# import csv
# class User:
#     def __init__(self,username,password):
#         self.username = username
#         self.password = password
#
#     @staticmethod
#     def register():
#         file_path = 'login_info.csv'
#         df_account = pd.read_csv(file_path)
#         list_username = list(df_account['username'])
#         while True:
#             username = input('please enter username')
#             if username in list_username:
#                 print('username exists!')
#             else:
#                 break
#         password = input('please enter password')
#         hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
#         object_user = User(username, hashed_password)
#         row_account = [[object_user.username, object_user.password]]
#         with open(file_path, 'a', newline='') as csv_account:
#             csv_writer = csv.writer(csv_account)
#             # writing the data row
#             csv_writer.writerows(row_account)


##make a file named main.py
from administrator import Administrator
from student import Student
from user import User
import pickle

# with open('shimi.txt','rb') as f:
#     x=pickle.load(f)
#     for l in x:
#         print(l.name)
while True:
    print("------------------------------------------")
    selected_item = input("what do you want to do?\n1-log in\n2-sign up\n3-exit\nyour choice: ")
    if selected_item == '1':
        user = User.log_in()
        if isinstance(user, Administrator):
            while True:
                task = input("what do you want to do:\n1-import lessons\n2-accept or reject "
                             "a student's unit selection\n3-exit\nyour choice: ")
                if task == '1':
                    major = input("please enter major: ")
                    no_lessons = int(input("how many lessons do you want to import? "))
                    user.import_lessons(major, no_lessons)
                elif task == '2':
                    user.accept_reject_unit_selection()
                else:
                    break
        if isinstance(user, Student):
            while True:
                task = input("what do you want to do:\n1-take lessons\n"
                             "2-see selected lessons\n3-exit\nyour choice: ")
                if task == '1':
                    while True:
                        x = user.take_lessons(user.major)
                        if x is False:
                            break
                        else:
                            contnue = input("do you want to choose another lesson?y/n")
                            if contnue == 'n':
                                break
                elif task == '2':
                    user.see_selected_lessons()
                else:
                    break
    elif selected_item == '2':
        User.register()
    else:
        break
