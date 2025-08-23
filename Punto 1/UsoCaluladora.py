"""
Script principal para probar la clase CalculadoraCientifica.
Se realizan pruebas de operaciones matemáticas básicas y avanzadas,
así como manejo de errores.
"""

import sys
import os
import math
import importlib

# === Configuración del entorno ===
# Agregar la carpeta que contiene tu archivo al path
sys.path.append(
    r"C:\Users\Davd Lopez\Documents\Big Data\Taller #1\Punto 1\mini_library"
)

import mini_library  # Importación de librería personalizada

# Recargar en caso de cambios en la librería
importlib.reload(mini_library)

# Importar la calculadora científica
from Calculadora import CalculadoraCientifica


def main():
    """Función principal para ejecutar las pruebas de la calculadora."""

    print(f"Directorio de trabajo: {os.getcwd()}")
    print("=" * 60)

    # --- Punto 1: Suma ---
    print("Punto 1 - Suma")
    calc = CalculadoraCientifica(3.12, 6.0, "+")
    print(calc)
    calc.suma(5, 5)
    print(calc.resultado)
    print(calc)

    calc = CalculadoraCientifica(5, 3, "+")
    print(calc.suma())

    # --- Punto 2: Multiplicación ---
    print("=" * 60)
    print("Punto 2 - Multiplicación")
    calc = CalculadoraCientifica(10, 2)
    print(calc.multiplicacion())
    print(calc)

    # --- Punto 3 ---
    print("=" * 60)
    print("Punto 3")
    calc = CalculadoraCientifica(10, 2)
    print(calc)
    print(calc.multiplicacion())
    print(calc)

    # --- Punto 4: Raíz y potencia ---
    print("=" * 60)
    print("Punto 4 - Raíz y potencia")
    c1 = CalculadoraCientifica(3)
    print(c1.potencia(2))
    print(c1)

    c2 = CalculadoraCientifica(16)
    print(c2.raiz_cuadrada())
    print(c2)

    # --- Punto 5: Operaciones encadenadas ---
    print("=" * 60)
    print("Punto 5 - Operaciones encadenadas")
    calc = CalculadoraCientifica(10)
    result = calc.suma(5).multiplicacion(2)
    print(result.operando1)
    print(result)

    # --- Punto 6: Funciones trigonométricas ---
    print("=" * 60)
    print("Punto 6 - Funciones trigonométricas")
    calc = CalculadoraCientifica()
    calc.operando1 = math.pi / 2
    print("Seno:", calc.seno())        # Espera: 1.0
    print("Coseno:", calc.coseno())    # Espera: cercano a 0
    print("Tangente:", calc.tangente())

    # --- Punto 7: Manejo de errores ---
    print("=" * 60)
    print("Punto 7 - Manejo de errores")
    calc = CalculadoraCientifica()
    print("---- PRUEBAS DIVISIÓN POR CERO ----")
    print(calc.division(10, 0))
    print("---- PRUEBAS NO NUMÉRICOS ----")
    print(calc.suma("a", 2))

    # --- Ejecución de pruebas unitarias en mini_library ---
    print("=" * 60)
    print("Pruebas en mini_library")
    mini_library.pruebas()


if __name__ == "__main__":
    main()
