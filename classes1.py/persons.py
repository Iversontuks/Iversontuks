class Person:
    def __init__(self,_name,_age):
        self.name = _name
        self.age = _age

    def sayHi(self):
        print('Hello,my name is ' + self.name + ' and i am ' + self.age + ' years old')
person1 = Person('Bob',str(18))
person2 = Person('James',str(22))
person1.sayHi()
print("\n")
person2.sayHi()


    