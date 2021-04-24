from person import Person


class Student(Person):
    students = list()

    def __init__(self, name, family_name, student_number,
                 major, no_units=0, lessons=list()):
        super().__init__(name, family_name)
        self.student_number = student_number
        self.major = major
        Student.students.append(self)
        self.no_units = no_units
        self.lessons = lessons

    def choose_lesson(self, lesson):
        """
        the student chooses a lesson, first is_valid_no_units method is checked
        and if the student is allowed to take the lesson, it is added to the
        student's lessons list, then update_status method for the lesson is called
        """

    def is_valid_no_units(self):
        """
        returns (True, True) if number of units taken by the student is
         greater than 10 and less than 20
        """

    def show_lessons(self):
        """
        shows the list of the student's lessons
        """