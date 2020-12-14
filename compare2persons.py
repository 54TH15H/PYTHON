class person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(' NAME : {} \n AGE  : {}'.format(self.name, self.age))

    def com(self, other):
        if self.name == other.name and self.age == other.age:
            print(' THOSE PERSONS ARE SAME')
        else:
            print(' THOSE ARE DIFFERENT PERSONS')

n1 = input('Enter name of First person : ')
a1 = int(input('Enter age of First person : '))
n2 = input('Enter name of Second person : ')
a2 = int(input('Enter age of Second person : '))

p1 = person(n1.lower(), a1)
p2 = person(n2.lower(), a2)

p1.details()
p2.details()

p1.com(p2)

