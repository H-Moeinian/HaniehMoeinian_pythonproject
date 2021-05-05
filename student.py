import pickle
from lesson import Lesson
import csv


class Student:

    def __init__(self, username, major=None, no_units=0, lessons=""):
        self.username = username
        self.major = major
        self.no_units = no_units
        self.lessons = lessons

    def take_lessons(self, major):
        with open(f"{major}.txt", 'rb') as my_file:
            lessons = pickle.load(my_file)
            print("------------------------------------------")
            print("this is the list of lessons you are allowed to take:")
            for i, lsson in enumerate(lessons):
                print(f"{i+1}-name: {lsson.name}, teacher: {lsson.teacher},"
                      f" units: {lsson.units}, capacity: {lsson.capacity}")
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
        with open('students.csv', 'w', newline='') as my_file:
            csv_writer = csv.writer(my_file)
            csv_writer.writerows(students)

    def see_selected_lessons(self):
        with open('students.csv', 'r') as f:
            students = list(csv.reader(f))
            for i in students:
                if self.username == i[0]:
                    print(f"these are the lessons you have taken:\n{i[3].strip()[:-1]}\n"
                          f"number of units you have taken: {i[2]}")





if __name__ == "__main__":
    x = Student('asdf')

