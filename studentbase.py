from random import randint


class Student: # определения студента в базу
    def __init__(self, name, age, evaluation):
        self.__name = name
        self.__age = age
        self.__ticket = randint(0,100000)
        self.__evaluation = list(map(int, evaluation.split()))

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    @property
    def ticket(self):
        return self.__ticket
    
    @ticket.setter
    def ticket(self, ticket):
        self.__ticket = ticket

    @property
    def evaluation(self):
        return self.__evaluation

    @evaluation.setter
    def evaluation(self, evaluation):
        self.__evaluation = evaluation

    @property
    def average(self):
        return sum(self.__evaluation) / len(self.__evaluation)
    
