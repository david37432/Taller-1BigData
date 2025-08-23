"""
Created on Wed Aug 2, 2025
@author: Martin Jerez
"""
import math

class Calculadora:
    """
    Implementa una calculadora
    """
    tipo = 'cientifica'
    
    def __init__(self, operando1=0, operando2=0, operacion=None):
        self.operando1 = operando1
        self.operando2 = operando2
        self.operacion = operacion
        self.resultado = None
    
    def __str__(self):
        if self.operacion is None:
            return "Calculadora en espera"
        if self.resultado is not None:
            return f"{self.operando1} {self.operacion}{self.operando2 if self.operacion not in ['√'] else ''} = {self.resultado}"
        return f"{self.operando1} {self.operacion} {self.operando2}"
    
    def suma(self, operando1=None, operando2=None):
        self.operacion = "+"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        
        try:
            resultado = self.operando1 + self.operando2
            self.operando1 = resultado
            self.resultado = resultado
            return self
        except TypeError:
            print("Error: Los operandos deben ser valores numéricos.")
            self.resultado = None
            return None
    
    def resta(self, operando1=None, operando2=None):
        self.operacion = "-"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        
        try:
            resultado = self.operando1 - self.operando2
            self.operando1 = resultado
            self.resultado = resultado
            return self
        except TypeError:
            print("Error: Los operandos deben ser valores numéricos.")
            self.resultado = None
            return None
    
    def multiplicacion(self, operando1=None, operando2=None):
        self.operacion = "*"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        
        try:
            resultado = self.operando1 * self.operando2
            self.operando1 = resultado
            self.resultado = resultado
            return self
        except TypeError:
            print("Error: Los operandos deben ser valores numéricos.")
            self.resultado = None
            return None
    
    def division(self, operando1=None, operando2=None):
        self.operacion = "/"
        if operando1 is not None and operando2 is not None:
            self.operando1 = operando1
            self.operando2 = operando2
        elif operando1 is not None and operando2 is None:
            self.operando2 = operando1
        
        try:
            resultado = self.operando1 / self.operando2
            self.operando1 = resultado
            self.resultado = resultado
            return self
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")
            self.resultado = None
            return None
        except TypeError:
            print("Error: Los operandos deben ser valores numéricos.")
            self.resultado = None
            return None
    
    def potencia(self, exponente):
        self.operacion = f'^ {exponente}'
        try:
            self.resultado = self.operando1 ** exponente
            return self.resultado
        except TypeError:
            print("Error: El operando debe ser un valor numérico.")
            self.resultado = None
            return None
    
    def raiz_cuadrada(self):
        self.operacion = '√'
        try:
            self.resultado = math.sqrt(self.operando1)
            return self.resultado
        except ValueError as e:
            print("Error de raíz cuadrada:", e)
            self.resultado = None
            return "valor no definido"
        except TypeError:
            print("Error: El operando debe ser un valor numérico.")
            self.resultado = None
            return None


class CalculadoraCientifica(Calculadora):
    """
    Calculadora científica que hereda de Calculadora
    y agrega funciones trigonométricas
    """
    def seno(self):
        self.operacion = "sin"
        try:
            self.resultado = math.sin(self.operando1)
            return self.resultado
        except TypeError:
            print("Error: El operando debe ser un valor numérico.")
            self.resultado = None
            return None

    def coseno(self):
        self.operacion = "cos"
        try:
            self.resultado = math.cos(self.operando1)
            return self.resultado
        except TypeError:
            print("Error: El operando debe ser un valor numérico.")
            self.resultado = None
            return None

    def tangente(self):
        self.operacion = "tan"
        try:
            self.resultado = math.tan(self.operando1)
            return self.resultado
        except TypeError:
            print("Error: El operando debe ser un valor numérico.")
            self.resultado = None
            return None
