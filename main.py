import csv
import hashlib
from student import Student
from administrator import Administrator
from user import User
import logging

my_logger = logging.getLogger('logger')
file_handler = logging.FileHandler('file.log')
file_handler.setLevel(logging.DEBUG)
s_format = logging.Formatter('%(levelname)s-%(asctime)s-%(name)s-%(message)s')
file_handler.setFormatter(s_format)
my_logger.addHandler(file_handler)
my_logger.setLevel(logging.DEBUG)

try:
    with open('user_info.csv', 'r') as f:
        user_info = list(csv.reader(f))
        del user_info[0]
except OSError:
    print("an error occurred while opening the file user_info.csv")
    my_logger.error("an error occurred while opening the file user_info.csv")
try:
    with open('locked_users.txt', 'r') as f:
        locked_users = f.readlines()
except OSError:
    print("an error occurred while opening the file")
    my_logger.error("an error occurred while opening the file locked_users.txt")
try:
    with open('courses.csv', 'r') as f:
        courses = list(csv.reader(f))
        del courses[0]
except OSError:
    print("an error occurred while opening the file")
    my_logger.error("an error occurred while opening the file courses.csv")


while True:
    print("------------------------------------------")
    try:
        selected_item = input("what do you want to do?\n1-log in\n2-sign up\n3-exit\nyour choice: ")
        assert selected_item in ['1', '2', '3']
    except AssertionError:
        print("wrong input! you should enter one of the numbers 1, 2 or 3")
        my_logger.error("wrong input in line 39 of main.py")
    else:
        if selected_item == '1':
            username = input("please enter your username: ")
            if User.is_locked(locked_users, username):
                continue
            else:
                for row in user_info:
                    if row[0] == username:
                        password, role, major = row[1], row[2], row[3]
                        break
                else:
                    print("there is not such a user!")
                    continue
                user = User(username, password, role, major)
                correct_log_in = user.log_in(locked_users)
                if correct_log_in:
                    my_logger.info(f"{user.username} entered the system successfully")
                if not correct_log_in:
                    my_logger.info(f"{user.username} could not enter the system")
                    continue
                else:
                    if user.role == 'student':
                        user = Student(user.username, user.hashed_password, user.role, user.major)
                        while True:
                            try:
                                task = input("what do you want to do:\n1-take lessons\n"
                                             "2-see selected lessons\n3-omit a lesson\n"
                                             "4-exit\nyour choice: ")
                                assert task in ['1', '2', '3', '4']
                            except AssertionError:
                                print("wrong input! you should enter one of the numbers 1, 2, 3 or 4")
                                my_logger.error("wrong input in line 69 of main.py")
                            else:
                                if task == '1':
                                    while True:
                                        x = user.take_lessons(user_info, courses, my_logger)
                                        if x is False:
                                            break
                                        else:
                                            while True:
                                                try:
                                                    contnue = input("do you want to choose another course?y/n ")
                                                    assert contnue in ['y', 'n']
                                                except AssertionError:
                                                    print("")
                                                else:
                                                    break

                                            if contnue == 'n':
                                                break
                                elif task == '2':
                                    print("----------------------------------------")
                                    print("these are your lessons in this semester: ")
                                    user.see_selected_courses(user_info)
                                elif task == '3':
                                    print("----------------------------------------")
                                    user.see_selected_courses(user_info)
                                    for usr in user_info:
                                        if usr[0] == user.username:
                                            if int(usr[4]) != 0:
                                                try:
                                                    course_no = int(input("which course do you want to omit? ")) - 1
                                                except ValueError:
                                                    print("you should enter a number")
                                                    my_logger.error("wrong input in line 105 of main.py")
                                                else:
                                                    user.omit_course(user_info, course_no, courses)
                                elif task == '4':
                                    break

                    else:
                        user = Administrator(user.username, user.hashed_password, user.role, user.major)
                        while True:
                            try:
                                task = input("what do you want to do:\n1-import lessons\n2-accept or reject "
                                             "a student's unit selection\n3-exit\nyour choice: ")
                                assert task in ['1', '2', '3']
                            except AssertionError:
                                print("you should enter one of the values 1, 2 or 3")
                                my_logger.error("wrong input in line 118 of main.py")
                            else:
                                if task == '1':
                                    while True:
                                        try:
                                            no_courses = int(input("how many lessons do you want to import? "))
                                        except ValueError:
                                            print("you should enter a number")
                                            my_logger.error("wrong input in line 128 of main.py")
                                        else:
                                            break
                                    for course in range(no_courses):
                                        print("------------------------------------------")
                                        name = input("enter course's name: ")
                                        teacher = input("enter course's teacher: ")
                                        major = input("enter course's major: ")
                                        units = input("enter course's units: ")
                                        capacity = input("enter course's capacity: ")
                                        print("------------------------------------------")
                                        user.import_lesson(courses, name, teacher, major, units, capacity)
                                        my_logger.info(f"course {name} was added to the system")
                                elif task == '2':
                                    print("------------------------------------------")
                                    print('students: ')
                                    for usr in user_info:
                                        if usr[2] == 'student':
                                            print(f"{usr[0]}")
                                    stu = input("which student's unit selection do you want to check?\n"
                                                "enter a name:  ")
                                    print("------------------------------------------")
                                    user.accept_reject_unit_selection(user_info, stu, my_logger)
                                elif task == '3':
                                    break
        elif selected_item == '2':
            try:
                student_or_administrator = input("are you a student or an administrator?\n"
                                                 "1-student\n2-administrator\nyour choice: ")
                assert student_or_administrator in ['1', '2']
            except AssertionError:
                print("you should enter one of the values 1 or 2")
                my_logger.error("wrong input in line 157 of main.py")
            else:
                if student_or_administrator == '2':
                    key = input("please enter the security key: ")
                    if key != 'a1z9f4':
                        print("wrong security key. you can not register as an administrator!")
                        continue
                print("------------------------------------------")
                while True:
                    username = input('please enter username: ')
                    for user in user_info:
                        if username == user[0]:
                            print('there is a user with this username! please choose another username.')
                    else:
                        break
                password = input('please enter password: ')
                hashed_password = hashlib.sha256(password.encode('utf8')).hexdigest()
                if student_or_administrator == '1':
                    major = input("please enter your major: ")
                else:
                    major = None
                role = {'1': 'student', '2': 'administrator'}
                user = User(username, hashed_password, role[student_or_administrator], major)
                user.register(user_info)
        elif selected_item == '3':
            try:
                with open('user_info.csv', 'w', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(['username','password','role','major','no_units','courses'])
                    csv_writer.writerows(user_info)
            except OSError:
                print(f"an error occurred while working with the file")
                my_logger.error("error while writing in file user_info.csv")
            try:
                with open('locked_users.txt', 'w') as f:
                    f.writelines(locked_users)
            except OSError:
                print(f"an error occurred while working with the file")
                my_logger.error("error while writing in file locked_users.txt")
            try:
                with open('courses.csv', 'w', newline='') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerow(['name','teacher','major','units','capacity','active'])
                    csv_writer.writerows(courses)
                    break
            except OSError:
                print(f"an error occurred while working with the file")
                my_logger.error("error while writing in file courses.csv")




