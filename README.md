#  Project PY- CalculatorProject
### Generalitati 
In acest proiect am creat o varianta de calculator avansat, folosind limbaj Python, in care am implementat piloni OOP.

Astfel, calculatorul efectueaza operatiile aritmetice de adunare, scadere, inmultire si impartire,  iar in modul avansat, acesta efectueaza operații precum: modulo, ridicare la putere, dar  si functii avansate (radical, logaritm natural
si exponentiala)

### Pasii de urmat:
1. Am creat un Python Package cu denumirea _calculators_.
2. Am creat un fisier python cu denumirea _calculatorABC.py_ unde am creat clasa abstracta **calculatorABC(ABC)** care contine metoda abstracta calculate():
   
       from abc import ABC, abstractmethod
       class CalculatorABC(ABC):
            @abstractmethod
            def calculate(self):
                 pass
   
4. Am creat un fisier python cu denumirea _calculator_simplu.py_ unde am creat clasa **CalculatorSimplu()** și metodele necesare pentru operațiile de bază a unui
calculator simplu cu operații aritmetice (+, -, *, /), metoda de afișare a rezultatului si metoda calculate()

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
   
6. Am creat un fisier python cu denumirea _calculator_advance.py_ unde am creat clasa CalculatorAdvance() și metodele necesare unor operații precum: operații
aritmetice (modulo, ridicare la putere) si functii avansate (radical, logaritm natural si exponentiala), metoda de afișare a rezultatului si metoda calculate():

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
   
In fisierul _main.py_ - fisierul python principal- am rulat aplicatia.

    from calculators.calculator_simplu import CalculatorSimplu
    from calculators.calculator_advance import CalculatorAdvance

    Utilizare pentru CalculatorSimplu
    calcul_simplu = CalculatorSimplu(9, 2,)
    calcul_simplu.calculate('+')
    calcul_simplu.afisare_rezultat()

    calcul_simplu = CalculatorSimplu(11, 10,)
    calcul_simplu.calculate('-')
    calcul_simplu.afisare_rezultat()

    calcul_simplu = CalculatorSimplu(11, 2,)
    calcul_simplu.calculate('*')
    calcul_simplu.afisare_rezultat()

    calcul_simplu = CalculatorSimplu(4, 2,)
    calcul_simplu.calculate('/')
    calcul_simplu.afisare_rezultat()

     calcul_simplu = CalculatorSimplu(4, 0,)
     calcul_simplu.calculate('/')
     calcul_simplu.afisare_rezultat()
     
     Utilizare pentru CalculatorAdvance
     calcul_advance = CalculatorAdvance(18, 2)
     calcul_advance.calculate('%')
     calcul_advance.afisare_rezultat()

    calcul_advance = CalculatorAdvance(4, 2)
    calcul_advance.calculate('**')
    calcul_advance.afisare_rezultat()

    calcul_advance = CalculatorAdvance(25, 5)
    calcul_advance.calculate('sqrt')
    calcul_advance.afisare_rezultat()

    calcul_advance = CalculatorAdvance(100, 5)
    calcul_advance.calculate('log')
    calcul_advance.afisare_rezultat()

    calcul_advance = CalculatorAdvance(35, 5)
    calcul_advance.calculate('exp')
    calcul_advance.afisare_rezultat()
