#Importam cele doua clase si rulam aplicatia.

from calculators.calculator_simplu import CalculatorSimplu
from calculators.calculator_advance import CalculatorAdvance

# Utilizare pentru CalculatorSimplu
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

# calcul_simplu = CalculatorSimplu(4, 0,)
# calcul_simplu.calculate('/')
# calcul_simplu.afisare_rezultat()

# Utilizare pentru CalculatorAdvance
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




