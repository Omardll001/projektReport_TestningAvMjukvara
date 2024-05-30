import pickle

class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
    
    def print_info(self):
        print(self.name)
        print(self.age)

    def increaseage(self, num):
        self.age += num
    
# p1 = Person('Omar', 23)
# p1.print_info()
# p1.increaseage(5)
# p1.print_info()

# with open('testPerson.pickle', 'wb') as f:
#     pickle.dump(p1, f)

with open('testPerson.pickle', 'rb') as f:
    p1 = pickle.load(f)

p1.print_info()
