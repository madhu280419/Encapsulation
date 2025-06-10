class Person:
    def _init_(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            self.__age = "Invalid age"

    def display(self):
        print(f"Name: {self._name}, Age: {self._age}")

p = Person("jaunt", 31)
p.display()

p.set_age(26)
p.set_name("madhu")  
p.display(set)  