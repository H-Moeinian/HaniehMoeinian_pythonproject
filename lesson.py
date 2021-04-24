class Lesson:
    def __init__(self, name, teacher, units, capacity):
        self.name = name
        self.teacher = teacher
        self.units = units
        self.capacity = capacity

    def update_status(self):
        """
        each time a student chooses the lesson, its capacity reduces.
        """