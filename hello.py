class Dog:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name + "is now sitting")
    def roll_over(self):
        print(self.name + "rolled over")
my_dog = Dog('i', 'we')
your_dog = Dog('lucy', 3, )
print("my dogs name is " +your_dog.name)
your_dog.sit()
your_dog.roll_over()