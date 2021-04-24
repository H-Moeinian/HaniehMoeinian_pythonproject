from person import Person

class Administrator(Person):
    def __init__(self, name, family_name):
        self.name = name
        self.family_name = family_name

    def import_lessons(self):
        """
        administrator inserts lessons to the system. it returns the list of lessons
        """