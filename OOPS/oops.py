class Person:
    count = 0
    def __init__(self,age,name,profession):
        self.name = name
        self.age = age
        self.profession = profession


    def showdetails(self):
        print(f'name = {self.name}')
        print(f'age = {self.age}')
        print(f'profession = {self.profession}')
        print(Person.count,'object created')


p1 = Person('vivek',21,'developer')
p1.showdetails()

p2= Person('ashish',21,'python developer')
p1.name='vaibhav'
Person.count = 5
p1.showdetails()
p2.showdetails()


