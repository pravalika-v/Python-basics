class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"hello i am {self.name}")
        
        
p1 = Person("john")
p1.talk()