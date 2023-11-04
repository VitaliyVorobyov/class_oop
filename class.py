class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_hw_lecturer(self, lecturer, course, grade):
        if (isinstance(lecturer, Lecturer)
                and course in self.courses_in_progress
                and course in lecturer.courses_attached):
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def _mean_grades(self):
        result = sum([sum(grade) for grade in self.grades.values()])/sum([len(grade) for grade in self.grades.values()])
        return result

    def __str__(self):
        if not self.finished_courses:
            return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {self._mean_grades()}\n'
                    f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                    f'Завершенные курсы: Нет завершенных курсов')
        else:
            return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                    f'Средняя оценка за лекции: {self._mean_grades()}\n'
                    f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'
                    f'Завершенные курсы: {", ".join(self.finished_courses)}')

    def __eq__(self, other):
        return self._mean_grades() == other

    def __lt__(self, other):
        return self._mean_grades() < other

    def __gt__(self, other):
        return self._mean_grades() > other


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def _mean_grades(self):
        result = sum([sum(grade) for grade in self.grades.values()])/sum([len(grade) for grade in self.grades.values()])
        return result

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._mean_grades()}'

    def __eq__(self, other):
        return self._mean_grades() == other

    def __lt__(self, other):
        return self._mean_grades() < other

    def __gt__(self, other):
        return self._mean_grades() > other


student_1 = Student('Ruoy', 'Eman', 'male')
student_1.courses_in_progress += ['Python', 'Git']
student_1.finished_courses += ['Введение в программирование']

student_2 = Student('Lisa', 'Task', 'female')
student_2.courses_in_progress += ['Python', 'Git']
student_2.finished_courses += ['Введение в программирование']

reviewer_1 = Reviewer('Some', 'Buddy')
reviewer_1.courses_attached += ['Python', 'Git']
reviewer_1.rate_hw(student_1, 'Python', 10)
reviewer_1.rate_hw(student_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'Git', 10)
reviewer_1.rate_hw(student_1, 'Git', 8)

reviewer_2 = Reviewer('Fill', 'Bud')
reviewer_2.courses_attached += ['Python', 'Git']
reviewer_2.rate_hw(student_2, 'Python', 9)
reviewer_2.rate_hw(student_2, 'Python', 6)
reviewer_2.rate_hw(student_2, 'Git', 8)
reviewer_2.rate_hw(student_2, 'Git', 7)

lecturer_1 = Lecturer('Ilon', 'Mask')
lecturer_1.courses_attached += ['Python', 'Git']
student_1.rate_hw_lecturer(lecturer_1, 'Python', 10)
student_1.rate_hw_lecturer(lecturer_1, 'Python', 7)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 10)
student_1.rate_hw_lecturer(lecturer_1, 'Git', 6)

lecturer_2 = Lecturer('Cris', 'Nolan')
lecturer_2.courses_attached += ['Python', 'Git']
student_2.rate_hw_lecturer(lecturer_2, 'Python', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Python', 4)
student_2.rate_hw_lecturer(lecturer_2, 'Git', 10)
student_2.rate_hw_lecturer(lecturer_2, 'Git', 6)
print('Студенты:')
print()
print(student_1)
print()
print(student_2)
print('--------------')
print('Проверяющие:')
print()
print(reviewer_1)
print()
print(reviewer_2)
print('--------------')
print('Лекторы:')
print()
print(lecturer_1)
print()
print(lecturer_2)
print('--------------')
print('Сравнение лекторов и студентов:')
print()
print(student_2 < student_1)
print(lecturer_1 == lecturer_2)
print('--------------')


def mean_students(course_name, *args):
    grade_sum = 0
    for student in args:
        grade_sum += sum(student.grades[course_name]) / len(student.grades[course_name])
    result = grade_sum / len(args)
    return f'Средняя оценка студентов в рамках курса "{course_name}" - {result}'


def mean_lecturer(course_name, *args):
    grade_sum = 0
    for lecturer in args:
        grade_sum += sum(lecturer.grades[course_name]) / len(lecturer.grades[course_name])
    result = grade_sum / len(args)
    return f'Средняя оценка лекторов в рамках курса "{course_name}" - {result}'


print(mean_students('Git', student_1, student_2))
print(mean_students('Python', student_1, student_2))
print(mean_lecturer('Git', lecturer_1, lecturer_2))
print(mean_lecturer('Python', lecturer_1, lecturer_2))
