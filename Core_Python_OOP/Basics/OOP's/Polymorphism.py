#Polymorphism, mainly for like it allows 2 classes use the same name methods but perform different actios

class Employee():
    def work(self):
        print("Working...")

class Developer(Employee):
    def work_part(self):
        super().work()

    def work(self):
        print("ok...")

class Tester(Employee):
    def work_test(self):
        super().work()
    def work(self):
        print("test,test....")


e = Employee()

e.work()

d = Developer()

d.work_part()
d.work()

t = Tester()
t.work_test()
t.work()
