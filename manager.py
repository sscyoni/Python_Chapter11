class Employee :
    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary
    
    def getSalary(self):
        return salary

class Manager(Employee) :
    def __init__(self,name,salary,bonus) :
        super ().__init__(name,salary)
        self.bonus = bonus

    def getsalary(self):
        salary = super ().getSalary()
        return salary + self.bonus
    
    def __repr__(self):
        return (f"이름{self.name}, 월급 {self.salary},보너스{self.bonus}")

kim=Manager('김철수',200000,100000)
print(kim)