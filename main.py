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
            courses_grades = lecturer.grades.values()
            all_grades = []
            for grade_list in courses_grades:
                all_grades.extend(grade_list)
            lecturer._average = sum(all_grades) / len(all_grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average}\n'
                f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: '
                f'{", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self._average == other._average

    def __ne__(self, other):
        return self._average != other._average

    def __lt__(self, other):
        return self._average < other._average

    def __add__(self, other):
        return self._average + other._average

    def __mul__(self, other):
        return self._average * other._average

    def __neg__(self):
        return -self._average


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self._average = 0
        self.grades = {}

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average}'

    def __eq__(self, other):
        return self._average == other._average

    def __ne__(self, other):
        return self._average != other._average

    def __lt__(self, other):
        return self._average < other._average

    def __add__(self, other):
        return self._average + other._average

    def __mul__(self, other):
        return self._average * other._average

    def __neg__(self):
        return -self._average


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
            courses_grades = student.grades.values()
            all_grades = []
            for grade_list in courses_grades:
                all_grades.extend(grade_list)
            student._average = sum(all_grades) / len(all_grades)
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def average_students_on_course(students_list, course):
    all_course_grades = []
    for student in students_list:
        if not isinstance(student, Student):
            return f'Ошибка: студента "{student}" не существует'
        elif course in student.grades:
            all_course_grades.extend(student.grades[course])
    if all_course_grades:
        return round(sum(all_course_grades) / len(all_course_grades), 2)
    else:
        return 'Ошибка'

def average_lecturers_of_course(lecturers_list, course):
    all_course_grades = []
    for lecturer in lecturers_list:
        if not isinstance(lecturer, Lecturer):
            return f'Ошибка: лектора "{lecturer}" не существует'
        elif course in lecturer.grades:
            all_course_grades.extend(lecturer.grades[course])
    if all_course_grades:
        return round(sum(all_course_grades) / len(all_course_grades), 2)
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

print(best_student, '\n')
print(first_student, '\n')
print(cool_reviewer, '\n')
print(coolest_lecturer, '\n')
print(big_lecturer, '\n')
print(best_student == first_student)
print(best_student != first_student)
print(best_student > first_student)
print(best_student < first_student)
print(best_student + first_student)
print(best_student * first_student)
print(-best_student)
print(coolest_lecturer == big_lecturer)
print(coolest_lecturer != big_lecturer)
print(coolest_lecturer > big_lecturer)
print(coolest_lecturer < big_lecturer)
print(coolest_lecturer + big_lecturer)
print(coolest_lecturer * big_lecturer)
print(-coolest_lecturer)
print(average_students_on_course([best_student, first_student], 'Python'))
print(average_students_on_course([best_student, first_student], 'Giton'))
print(average_lecturers_of_course([coolest_lecturer, big_lecturer], 'Python'))