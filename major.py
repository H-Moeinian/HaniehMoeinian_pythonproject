class Major:
    def __init__(self, major_name, *lessons):
        self.major_name = major_name
        self.lessons = list(lessons)

    def show_major_lessons(self):
        """
        shows the list of lessons available for major
        """