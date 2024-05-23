#!/usr/bin/python3


class Student:

    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    # public method
    def bmi(self):
        return self.weight / (self.height / 100.0) ** 2

    # private method
    def __is_fat(self):
        return True if self.bmi() >= 35 else False

if __name__ == '__main__':
    students = [
        Student('bill', 169, 100),
        Student('brian', 164, 56),
        Student('eagle', 173, 20)
    ]

    for student in students:
        if student.overweight():
            print(student.name)
