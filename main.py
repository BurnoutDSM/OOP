class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.finished_coursed = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
            \rФамилия: {self.surname}
            \rСредняя оценка за лекцию: {self.calculate_average_grade_student()}
            \rКурсы в процессе обучения: {", ".join(self.courses_in_progress)}
            \rЗавершенные курсы: {", ".join(self.finished_coursed)}
        '''

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if 11 > grade > 0:
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            return 'Оценка не соответсвут критериям'
        return 'Ошибка'

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Лектор отсутствует')
        return self.calculate_average_grade_student() == other.calculate_average_grade_lecturer()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Лектор отсутствует')
        return self.calculate_average_grade_student() < other.calculate_average_grade_lecturer()

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            raise Exception('Лектор отсутствует')
        return self.calculate_average_grade_student() <= other.calculate_average_grade_lecturer()

    def calculate_average_grade_student(self):
        all_grades = []
        if not self.grades:
            return 0
        for grade in self.grades.values():
            all_grades += grade
        return round(sum(all_grades) / len(all_grades), 1)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def __str__(self):
        return f'''Имя: {self.name}
            \rФамилия: {self.surname}
            \rСредняя оценка за лекцию: {self.calculate_average_grade_lecturer()}
        '''

    def __eq__(self, other):
        if not isinstance(other, Student):
            raise Exception('Студент отсутствует')
        return self.calculate_average_grade_lecturer() == other.calculate_average_grade_student()

    def __le__(self, other):
        if not isinstance(other, Student):
            raise Exception('Студент отсутствует')
        return self.calculate_average_grade_lecturer() < other.calculate_average_grade_student()

    def __lt__(self, other):
        if not isinstance(other, Student):
            raise Exception('Студент отсутсвует')
        return self.calculate_average_grade_lecturer() <= other.calculate_average_grade_student()

    def calculate_average_grade_lecturer(self):
        all_grades = []
        if not self.grades:
            return 0
        for grade in self.grades.values():
            all_grades += grade
        return round(sum(all_grades) / len(all_grades), 1)


class Reviewer(Mentor):
    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if grade < 11 and grade > 0:
                if course in student.grades:
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
        else:
            return 'Ошибка'



    #Студенты
jesse_student = Student('Jesse', 'Pinkman', 'boy')
harry_student = Student('Harry', 'Potter', 'boy')

    #Лекторы
walter_lecturer = Lecturer('Walter', 'White')
hannibal_lecturer = Lecturer('Hannibal', 'Lecter')

    #Эксперты
hank_reviewer = Reviewer('Hank', 'Schrader')
harley_reviewer = Reviewer('Harley', 'Quinn')

    #Курсы студентов(в процессе обучения)
jesse_student.courses_in_progress += ['Python']
jesse_student.courses_in_progress += ['Git']
harry_student.courses_in_progress += ['Python']
harry_student.courses_in_progress += ['Git']

    #Завершненные курсы студентов
jesse_student.finished_coursed += ['Введение в программирование']
harry_student.finished_coursed += ['Введение в программирование']

    #Курсы лекторов
walter_lecturer.courses_attached += ['Python']
walter_lecturer.courses_attached += ['Git']
hannibal_lecturer.courses_attached += ['Python']
hannibal_lecturer.courses_attached += ['Git']

    #Оценки студентов
hank_reviewer.rate_hw(jesse_student, 'Python', 10)
hank_reviewer.rate_hw(jesse_student, 'Python', 9)
hank_reviewer.rate_hw(harry_student, 'Python', 9)
hank_reviewer.rate_hw(harry_student, 'Python', 8)
harley_reviewer.rate_hw(jesse_student, 'Git', 8)
harley_reviewer.rate_hw(jesse_student, 'Git', 9)
harley_reviewer.rate_hw(harry_student, 'Git', 10)
harley_reviewer.rate_hw(harry_student, 'Git', 8)

    #Оценки преподователей (от студентов)
jesse_student.rate_lecturer(walter_lecturer, 'Python', 10)
jesse_student.rate_lecturer(walter_lecturer, 'Git', 9)
jesse_student.rate_lecturer(hannibal_lecturer, 'Python', 9)
jesse_student.rate_lecturer(hannibal_lecturer, 'Git', 9)
harry_student.rate_lecturer(walter_lecturer, 'Python', 10)
harry_student.rate_lecturer(walter_lecturer, 'Git', 10)
harry_student.rate_lecturer(hannibal_lecturer, 'Python', 10)
harry_student.rate_lecturer(hannibal_lecturer, 'Git', 7)

    #Списки по принадлежности
students = [jesse_student, harry_student]
lecturers = [walter_lecturer, hannibal_lecturer]
reviewers = [hank_reviewer, harley_reviewer]

def compare_people(student, lecturer):
    if student.calculate_average_grade_student() < lecturer.calculate_average_grade_lecturer():
        return f'Соотношение оценок: {student.surname} {student.calculate_average_grade_student()} < {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'

    elif student.calculate_average_grade_student() > lecturer.calculate_average_grade_lecturer():
        return f'Соотношение оценок: {student.surname} {student.calculate_average_grade_student()} > {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'

    elif student.calculate_average_grade_student() == lecturer.calculate_average_grade_lecturer():
        return f'Соотношение оценок: {student.surname} {student.calculate_average_grade_student()} = {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'
    else:
        return 'Что-то пошло не так'


def calculate_average_grade_course(persons, course):
    if not isinstance(persons, list):
        return 'Нет списка'
    course_grade = []
    for person in persons:
        if course in person.grades:
            course_grade += person.grades[course]
    if course_grade == []:
        return 'По данному курсу оценок нет'

    return round(sum(course_grade) / len(course_grade), 1)


print(harry_student)
print(jesse_student != hannibal_lecturer)
print(calculate_average_grade_course(students, 'Python'))
print(calculate_average_grade_course(lecturers, 'Git'))
print(compare_people(jesse_student, walter_lecturer))
print(hannibal_lecturer.calculate_average_grade_lecturer())
print(jesse_student.calculate_average_grade_student())
