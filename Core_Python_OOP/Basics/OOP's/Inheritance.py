#Inheritance, mainly for code reuse and reduces duplicate code
class Employee():
    def work(self):
        print("Working...")

class Developer(Employee):

    # def work(self):
    #     print("Working....")

    def code(self):
        print("coding....")

class Tester(Employee):

    # def work(self):
    #     print("Working...")
    
    def test(self):
        print("Testing...")

d = Developer()
d.work()
d.code()

t = Tester()
t.work()
t.test()
