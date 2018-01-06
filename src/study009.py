# -*-coding: utf-8 -*-
from types import MethodType


class Student:
    __slots__ = ("name", "age", "set_age", "score", "set_score")
    pass


print(dir(Student))
s = Student()
s.name = "Jim"
print(s.name)


def set_age(self, age):
    self.age = age


s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age)


def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, Student)
s.set_score(90)
print(s.score)

s2 = Student()
s2.set_score(100)
print(s2.score)


class Teacher(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


t1 = Teacher();
t1.birth = 1987
print(t1.birth)
print(t1.age)




