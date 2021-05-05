import pickle


class Lesson:
    def __init__(self, name, teacher, units, capacity, active = True):
        self.name = name
        self.teacher = teacher
        self.units = units
        self.capacity = int(capacity)
        self.active = active

    def __str__(self):
        return f"lesson name: {self.name}, teacher: {self.teacher}, units: {self.units}, " \
               f"capacity: {self.capacity}"

    @staticmethod
    def update_status(major, lesson):
        """
        each time a student chooses the lesson, its capacity reduces.
        """
        with open(f"{major}.txt",'rb') as my_file:
            lessons = pickle.load(my_file)
            for i in lessons:
                if i.name == lesson:
                    i.capacity -= 1
                    if i.capacity == 0:
                        i.active = False
        with open(f"{major}.txt", 'wb') as my_file:
            pickle.dump(lessons,my_file)



        # self.capacity -=1
if __name__ == "__main__":
    Lesson.update_status("shimi")
