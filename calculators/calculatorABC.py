# https://drive.google.com/file/d/118fTIXjeMbC_on9SaIVZ9_9VTobWPPyY/view
# https://drive.google.com/file/d/1vVDCPtvt8YCTU4gqfJUCXyevdZTg549a/view
#vom crea clasa abstracta ce va contine metoda abstracta calculate()

from abc import ABC, abstractmethod

class CalculatorABC(ABC):
    @abstractmethod
    def calculate(self):
        pass
    