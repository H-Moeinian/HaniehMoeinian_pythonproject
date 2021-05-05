import csv

from lesson import Lesson
import pickle


class Administrator:
    def __init__(self, username):
        self.username = username

    def import_lessons(self, major, no_lessons):
        """
        administrator inserts lessons to the system. it returns the list of lessons
        """
        lessons = []
        for lsn in range(no_lessons):
            print("------------------------------------------")
            name = input("enter lesson's name: ")
            teacher = input("enter lesson's teacher: ")
            units = input("enter lesson's units: ")
            capacity = input("enter lesson's capacity: ")
            print("------------------------------------------")
            lesson = Lesson(name, teacher, units, capacity)
            lessons.append(lesson)
        with open(f"{major}.txt", 'ab') as lessons_file:
            pickle.dump(lessons, lessons_file)


    def accept_reject_unit_selection(self):
        print("------------------------------------------")
        print('students: ')
        with open('students.csv', 'r') as f:
            students = list(csv.reader(f))
            for i, stu in enumerate(students[1:]):
                print(i + 1, stu[0])
        stu = int(input("which student's unit selection do you want to check? "))
        print("------------------------------------------")
        print(f"{students[stu][0]}'s units:\n{students[stu][3].strip()[:-1]}")
        x = input("do you accept or reject this student's unit selection?\n1-accept\n"
                  "2-reject\nyour choice: ")
        if x=='1':
            return True
        else:
            students[stu][3]=""
            students[stu][2]=0
            with open('students.csv', 'w',newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerows(students)
            return False



