# -*- coding: utf-8 -*-
class Animal(object):
    pass


class Runnable(object):
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):
        print('Flying...')


class Mammal(Animal):
    pass


class Bird(Animal):
    pass


class Dog(Mammal, Runnable):
    pass


class Parrot(Bird, Flyable):
    pass


dog = Dog()
dog.run()
parrot = Parrot()
parrot.fly()


class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 500:
            raise StopIteration()
        return self.a

    def __getitem__(self, item):
        if isinstance(item, int):
            a, b = 1, 1
            for x in range(item):
                a, b = b, a + b
            return a
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            if step is None:
                step = 1
            for x in range(stop):
                if x >= start and x % step == 0:
                    L.append(a)
                a, b = b, a + b
            return L


for n in Fib():
    print(n)
print(Fib()[5])
print(Fib()[6:8])
print(Fib()[:12])
print(Fib()[:12:2])


class Chain(object):
    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain("%s/%s" % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


print(Chain().website.lucene.search.key)


class Student(object):
    def __init__(self, name):
        self._name = name

    def __call__(self, *args, **kwargs):
        print("My name is %s!" % self._name)


stu = Student("Jam")
stu()
print(callable(stu))
print(callable(max))
print(callable([1, 2, 3]))
