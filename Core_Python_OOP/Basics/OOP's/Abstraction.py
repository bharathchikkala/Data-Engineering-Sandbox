#Abstraction, hiding internal things shows only what users need
from abc import ABC,abstractmethod
class ATM(ABC):
    @abstractmethod
    def withdraw(self):
        pass


class SBI(ATM):
    def withdraw(self):
        print("Withdrawn from SBI")

class HDFC(ATM):
    def withdrawn(self):
        print("drawn from HDFC")

sbi = SBI()
sbi.withdraw()
