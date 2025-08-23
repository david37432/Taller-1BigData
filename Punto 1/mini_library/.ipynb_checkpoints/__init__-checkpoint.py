"""
Paquete mini_library
Este archivo inicializa la librería e incluye pruebas para todos los retos.
"""

import math
from Calculadora import Calculadora, CalculadoraCientifica

def pruebas():
    print("=== Challenge 1 & 2 & 3 ===")
    calc = Calculadora(5, 3, '+')
    print(calc.suma())
    print(calc.resta(10, 2))

    print("\n=== Challenge 4 ===")
    calc2 = Calculadora(9)
    print(calc2.raiz_cuadrada())
    print(calc2.potencia(2))

    print("\n=== Challenge 5 ===")
    resultado = Calculadora(10).suma(5).multiplicacion(2)
    print("Resultado encadenado:", resultado.operando1)

    print("\n=== Challenge 6 ===")
    cient = CalculadoraCientifica()
    cient.operando1 = math.pi / 2
    print("Seno:", cient.seno())
    print("Coseno:", cient.coseno())
    print("Tangente:", cient.tangente())

    print("\n=== Challenge 7 (Errores) ===")
    calc_error = Calculadora("a", 2)
    calc_error.suma()  


if __name__ == "__main__":
    pruebas()
