from stack import Stack
from abc import ABC

class Animal(ABC):
    def __init__(self, name):
        self.order = 0
        self.name = name

    def set_order(self, ord):
        self.order = ord

    def is_older_than(self, animal):
        return self.order < animal.order

class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalQueue():
    def __init__(self):
        self.dogs = Stack()
        self.cats = Stack()
        self.order = 0

    def enqueue(self, animal):
        animal.set_order(self.order)
        self.order += 1
        if type(animal) is Dog:
            self.dogs.push(animal)
        elif type(animal) is Cat:
            self.cats.push(animal)

    def dequeueAny(self):
        if self.dogs.is_empty():
            return self.dequeue_cats()
        elif self.cats.is_empty():
            return self.dequeue_dogs()

        dog = self.dogs.peek()
        cat = self.cat.peek()
        if dog.is_older_than(cat):
            return self.dequeue_dogs()
        else:
            return self.dequeue_cats()



    def dequeue_cats(self):
        return self.cats.pop()

    def dequeue_dogs(self):
        return self.dogs.pop()
