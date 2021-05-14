import pickle
from lesson import Lesson
import csv


class Student:
    def __init__(self, username, major=None, no_units=0, lessons=None):
        self.username = username
        self.major = major
        self.no_units = no_units
        self.lessons = lessons

    def take_lessons(self, major):
        try:
            with open(f"{major}.txt", 'rb') as my_file:
                lessons = pickle.load(my_file)
                print("------------------------------------------")
                print("this is the list of lessons you are allowed to take:")
                for i, lsson in enumerate(lessons):
                    print(f"{i+1}-name: {lsson.name}, teacher: {lsson.teacher},"
                          f" units: {lsson.units}, capacity: {lsson.capacity}")
        except OSError as err:
            print(f"OS error: {err}")
        try:
            with open('students.csv','r',newline='') as my_file:
                students = list(csv.reader(my_file))
                for j, student in enumerate(students):
                    if student[0] == self.username:
                        while True:
                            if int(student[2])<20:
                                print()
                                lsn_no = int(input("which lesson do you want to choose? "))-1
                                if f"{lessons[lsn_no].name}" not in student[3].strip().split(','):

                                    if lessons[lsn_no].active == True:
                                        if int(lessons[lsn_no].units) + int(student[2])<20:
                                            students[j][3] = lessons[lsn_no].name + ',' +\
                                                             students[j][3]
                                            students[j][2] = int(lessons[lsn_no].units) +\
                                                             int(student[2])
                                            Lesson.update_status(major, lessons[lsn_no].name)
                                        else:
                                            print("you can not take more than 20 units in"
                                                  " a semester!")
                                            return False
                                    else:
                                            print("this lesson's capacity is full!")
                                else:
                                    print("you can not take a lesson two times in a semester!")
                            if int(students[j][2])<10:
                                print("you need to take at least 10 units")
                                continue
                            else:
                                break
        except OSError as err:
            print(f"OS error: {err}")
        try:
            with open('students.csv', 'w', newline='') as my_file:
                csv_writer = csv.writer(my_file)
                csv_writer.writerows(students)
        except OSError as err:
            print(f"OS error: {err}")

    def see_selected_lessons(self):
        try:
            with open('students.csv', 'r') as f:
                students = list(csv.reader(f))

                for i in students:
                    if self.username == i[0]:
                        print(f"#########\nthese are the lessons you have taken:"
                              f"\n{i[3].strip()[:-1]}\n"
                              f"number of units you have taken: {i[2]}\n#########")
        except OSError as err:
            print(f"OS error: {err}")

    def omit_lesson(self):
        try:
            with open('students.csv', 'r', newline='') as f:
                students = list(csv.reader(f))
                for student in students:
                    if student[0] == self.username:
                        list_lessons = student[3].strip()[:-1].split(',')
                        for i, lssn in enumerate(list_lessons):
                            print(f"{i + 1}-{lssn}")
                        lesson_no = int(input("which lesson do you want to omit? ")) - 1
                        with open(f'{self.major}.txt', 'rb') as f:
                            lsns = pickle.load(f)
                            for lesson in lsns:
                                if lesson.name == list_lessons[lesson_no]:
                                    print(lesson.name, lesson.units)
                                    unit = int(lesson.units)
                                    student[2] = int(student[2]) - unit
                                    break
                        list_lessons.remove(list_lessons[lesson_no])
                        student[3] = ','.join(list_lessons)
                        student[3] += ','
        except OSError as err:
            print(f"OS error: {err}")
        except ValueError as err:
            print(f"value error: {err}")
        try:
            with open('students.csv', 'w', newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(students)
        except OSError as err:
            print(f"OS error: {err}")



