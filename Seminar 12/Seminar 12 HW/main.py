# Создайте класс студента.
# * Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
# * Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие предметы в экземпляре недопустимы.
# * Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
# * Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам всех предметов вместе взятых.
import student_class as st

s = st.Student("Иван", "Иванов", "Иванович", "математика", 5, 87)
print(s.get_avg())
s.add_subject("русский", 3, 54)
s.add_subject('алгебра', 4, 66)
print(s.get_avg())
