class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_coursed = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if grade < 11 and grade > 0:
                if course in lecturer.grade_from_students:
                    lecturer.grade_from_students[course] += [grade]
                else:
                    lecturer.grade_from_students[course] = [grade]
            else:
                return 'Оценка не соответсвут критериям'
        else:
            return 'Ошибка'

    def calculate_average_grade_student(self):
        all_grades = []
        for grade in self.grades.values():
            all_grades += grade
        return round(sum(all_grades) / len(all_grades), 1)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.calculate_average_grade_student()} \nКурсы в процессе обучения: {self.courses_in_progress} \nЗавершенные курсы: {self.finished_coursed}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_from_students = {}

    def calculate_average_grade_lecturer(self):
        all_grades = []
        for grade in self.grade_from_students.values():
            all_grades += grade

        try:
            return round(sum(all_grades) / len(all_grades), 1)
        except:
            return 'что-то пошло не так'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname} \nСредняя оценка за лекцию: {self.calculate_average_grade_lecturer()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'


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
hank_reviewer.rate_hw(harry_student, 'Python', 10)
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


def compare_people(student, lecturer):
    # student = jesse_student
    # lecturer = walter_lecturer

    if student.calculate_average_grade_student() < lecturer.calculate_average_grade_lecturer():
        return f'{student.surname} {student.calculate_average_grade_student()} < {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'

    elif student.calculate_average_grade_student() > lecturer.calculate_average_grade_lecturer():
        return f'{student.surname} {student.calculate_average_grade_student()} > {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'

    elif student.calculate_average_grade_student() == lecturer.calculate_average_grade_lecturer():
        return f'{student.surname} {student.calculate_average_grade_student()} = {lecturer.surname} {lecturer.calculate_average_grade_lecturer()}'



def calculate_average_grade_course_stud(all_students, course):
    course_grade = []
    for student in all_students:
        if course in student.grades:
            course_grade += student.grades[course]
    try:
        return round(sum(course_grade) / len(course_grade), 1 )
    except:
        return 'что-то пошло не так'

def calculate_average_grade_course_lect(all_lecturer, course):
    course_grade = []
    for lecturer in all_lecturer:
        if course in lecturer.grade_from_students:
            course_grade += lecturer.grade_from_students[course]
    try:
        return round(sum(course_grade) / len(course_grade), 1)
    except:
        return 'что-то пошло не так'


print(calculate_average_grade_course_stud([jesse_student, harry_student], 'Python'))
print(calculate_average_grade_course_lect([hannibal_lecturer, walter_lecturer], 'Git'))