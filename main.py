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


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grade_from_students = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


best_student = Student('Jesse', 'Pinkman', 'boy')
best_student.courses_in_progress += ['python']

cool_lecturer = Lecturer('Walter', 'White')
cool_lecturer.courses_attached += ['python']

cool_reviewer = Reviewer('Hank', 'Schrader')
cool_reviewer.rate_hw(best_student, 'python', 10)
best_student.rate_lecturer(cool_lecturer, 'python', 10)
print(cool_lecturer.grade_from_students)