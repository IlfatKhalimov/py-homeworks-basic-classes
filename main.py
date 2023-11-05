class Student:
    def __init__(self, name, surname, gender):
        self._average = 0
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']
first_student = Student('Max', 'Mad', 'Male')
first_student.courses_in_progress += ['Python', 'Git']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']
good_reviewer = Reviewer('John', 'Smith')
good_reviewer.courses_attached += ['Python', 'Git']

coolest_lecturer = Lecturer('Dow', 'Jones')
coolest_lecturer.courses_attached += ['Python']
big_lecturer = Lecturer ('Stan', 'Big')
big_lecturer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
good_reviewer.rate_hw(best_student, 'Python', 8)
good_reviewer.rate_hw(best_student, 'Python', 8)
good_reviewer.rate_hw(best_student, 'Git', 9)
good_reviewer.rate_hw(first_student, 'Git', 6)
good_reviewer.rate_hw(first_student, 'Python', 7)

first_student.rate_lecture(coolest_lecturer, 'Python', 8)
best_student.rate_lecture(coolest_lecturer, 'Python', 6)

print(best_student.grades)
print(coolest_lecturer.grades)