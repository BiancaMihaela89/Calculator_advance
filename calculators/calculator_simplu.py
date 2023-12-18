# Cream clasa Calculator Simplu care extinde class abstracta si implementam metoda calculate.
from .calculatorABC import CalculatorABC

class CalculatorSimplu(CalculatorABC):
    def __init__(self, nr1, nr2):
        self.nr1 = nr1
        self.nr2 = nr2
        self.rezultat = None

    def calculate(self, operator):
        if operator == '+':
            self.rezultat = self.nr1 + self.nr2
        elif operator == '-':
            self.rezultat = self.nr1 - self.nr2
        elif operator == '*':
            self.rezultat = self.nr1 * self.nr2
        elif operator == '/':
            if self.nr2 != 0:
                self.rezultat = self.nr1 / self.nr2
            else:
                raise ZeroDivisionError("Al doilea parametru trebuie sa fie diferit de 0")
        else:
            raise ZeroDivisionError("Operatie invalida")

    def afisare_rezultat(self):
        if self.rezultat is not None:
            print("Rezultatul este:", self.rezultat)
        else:
            print("Rezultatul nu poate fi calculat")