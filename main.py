from studentbase import Student


class StudentManagementSystem: # работа с базой студентов
    def __init__(self):
        self._students = []
        self.quantity_students = 0

    def add_student(self, student):
        self._students.append(student)
        self.quantity_students += 1
        print(f'Студент с билетом - {student.ticket} успешно добавлен')

    def delete_student(self,ticket):
        for student in self._students:
            if student.ticket == int(ticket):
                self._students.remove(student)
                self.quantity_students -= 1
                print(f'Студент с билетом - {student.ticket} удален из базы.')
                return
        print('Студент по данному билету не найден')

    def check_students(self):
         print(f'В базе {self.quantity_students} студентов:')
         for student in self._students:
             print(f'Имя - {student.name};'
                   f' Возраст - {student.age};'
                   f' Билет - {student.ticket};' 
                   f' Оценки - {student.evaluation};' 
                   f' Средний балл = {student.average:.2f}')

if __name__ == '__main__':
    sm = StudentManagementSystem()
    
    while True:
        try:
            choice = int(input('Выберите действие над базой:'
                               '\n1. Добавить студента'
                               '\n2. Удалить студента'
                               '\n3. Просмотреть список студентов'
                               '\nВведите номер действия: '))
        
            if choice == 1:
                name = input('Введите имя студента: ')
                age = input('Введите возраст студента: ')
                evaluation = input('Введите оценки студента через пробел: ')
                student = Student(name,age,evaluation)
                sm.add_student(student)

            elif choice == 2:
                ticket = input('Введите билет студента: ')
                sm.delete_student(ticket)

            elif choice == 3:
                sm.check_students()
            else:
                print('Неверный номер действия. Пожалуйста, выберите 1, 2 или 3.')

        except ValueError:
            print('Введите корректный номер действия.')
    
