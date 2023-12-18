"""Cream clasa CalculatorAdvance care extinde clasa abstracta si
implementam metoda calculate. Importam modulul math pentru a avea
acces la functii matematice  avansate
"""
from .calculatorABC import CalculatorABC
import math

class CalculatorAdvance(CalculatorABC):
    def __init__(self, nr1, nr2):
        self.nr1 = nr1
        self.nr2 = nr2
        self.rezultat = None

    def calculate(self, operator):
        if operator == '%':
            self.rezultat = self.nr1 % self.nr2
        elif operator == '**':
            self.rezultat = self.nr1 ** self.nr2
        elif operator == 'sqrt':
            self.rezultat = math.sqrt(self.nr1)
        elif operator == 'log':
            self.rezultat = math.log(self.nr1)
        elif operator == 'exp':
            self.rezultat = math.exp(self.nr1)
        else:
            super().calculate(operator)

    def afisare_rezultat(self):
        if self.rezultat is not None:
            print("Rezultatul este :", self.rezultat)
        else:
            print("Rezultatul nu poate fi calculat")
