class Mammal :
    def __init__(self,species,age) :
        self. species =species
        self.age = age
    
class Person (Mammal):
    def __init__(self,species,age,name,job) :
      super ().__init__(species,age)
      self.name = name
      self.job = job
      

m1 = Mammal ("동물:",30)
p1 = Person("동물:",30,"kim","engineer")

print(f'포유류:{m1. age}, {m1. species}')
print(f'사람: {p1.age},{p1.job},{p1.name}')