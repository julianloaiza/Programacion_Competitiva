#!/usr/bin/env python3
"""
Plantilla básica de Python para Competencias,
con ejemplos de lectura de datos.
"""

import sys          # Para E/S rápida
import math         # Para gcd, etc.
import os           # Para leer variables de entorno, manejar archivos, etc.
import random       # Para aleatoriedad 
import re           # Para expresiones regulares

# Ajuste del límite de recursión (útil si se usan recursiones profundas).
sys.setrecursionlimit(10**7)

# ======================================================
#   Depuración Condicional
#   Se activa con: DEBUG=1 python3 main.py
# ======================================================
DEBUG = os.environ.get("DEBUG") is not None

def debug(*args):
    """
    Imprime en stderr únicamente si la variable de entorno DEBUG está activa.
    """
    if DEBUG:
        print(*args, file=sys.stderr)

# ======================================================
#   Constantes útiles
# ======================================================
INF = 10**15  # "Infinito" práctico
EPS = 1e-9    # Épsilon para comparaciones de flotantes

# ======================================================
#   Entrada/Salida Rápida
# ======================================================
def input_data():
    """
    Lectura de línea rápida equivalente a input() pero usando sys.stdin.readline().
    Elimina el salto de línea final.
    """
    return sys.stdin.readline().rstrip("\n")

def print_data(*args, sep=' ', end='\n'):
    """
    Salida rápida equivalente a print(), pero usando sys.stdout.write().
    """
    sys.stdout.write(sep.join(map(str, args)) + end)

# ======================================================
#   Funciones Matemáticas
# ======================================================
def gcd(a, b):
    """
    Máximo Común Divisor de a y b.
    (Python 3.9+ tiene math.gcd, lo reimplementamos por compatibilidad.)
    """
    return math.gcd(a, b)

def lcm(a, b):
    """
    Mínimo Común Múltiplo de a y b.
    (Python 3.9+ tiene math.lcm, lo reimplementamos por compatibilidad.)
    """
    return (a // gcd(a, b)) * b

def mod_exp(base, exp, mod):
    """
    Exponenciación modular rápida: (base^exp) % mod.
    """
    result = 1 % mod
    base %= mod
    while exp > 0:
        if exp & 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp >>= 1
    return result

# ======================================================
#   solve()
# ======================================================
def solve():
    """
    Aquí escribes la lógica para UN caso de prueba.
    Si hay múltiples testcases, la función solve() puede llamarse varias veces.
    """
    # Ejemplo simple de lectura dentro de solve():
    # line = input_data()
    # v, k = map(int, line.split())
    # answer = v + k
    # print_data(answer)
    pass

# ======================================================
#   main()
# ======================================================
def main():
    """
    Controla la lectura de datos y la llamada a solve().
    Aquí puedes adaptar distintos PATRONES de lectura (comentados abajo).
    """
    # Opción para leer y escribir desde archivos en local:
    # Activa esto con: LOCAL=1 python3 main.py
    if 'LOCAL' in os.environ:
        sys.stdin = open('input.txt', 'r')
        sys.stdout = open('output.txt', 'w')

    # -----------------------------------------------
    # Patrón 1: Lectura de T test cases (primera línea)
    # -----------------------------------------------
    # t = int(input_data())
    # for _ in range(t):
    #     # Llamamos a solve() que puede leer internamente
    #     solve()

    # -----------------------------------------------
    # Patrón 2: Leer hasta encontrar un '0'
    # -----------------------------------------------
    # while True:
    #     line = input_data()
    #     if not line:    # EOF
    #         break
    #     if line == "0": # Centinela '0' para terminar
    #         break
    #     # Procesas la línea
    #     x = int(line)
    #     # Por ejemplo, haz algo con x...
    #     # print_data(x*2)

    # -----------------------------------------------
    # Patrón 3: Leer hasta EOF
    # -----------------------------------------------
    # while True:
    #     line = input_data()
    #     if not line:  # Si ya no hay datos
    #         break
    #     # Procesar 'line'
    #     # ...
    
    # -----------------------------------------------
    # Patrón 4: Múltiples líneas por test case
    #    (por ejemplo, 3 líneas seguidas)
    # -----------------------------------------------
    # t = int(input_data())
    # for _ in range(t):
    #     line1 = input_data()  # primera línea del caso
    #     line2 = input_data()  # segunda línea
    #     line3 = input_data()  # tercera línea
    #     # parseas cada una
    #     # v1, k1 = map(int, line1.split())
    #     # ...
    #     # Procesas o llamas a solve_case(line1, line2, line3)

    # -----------------------------------------------
    # EJEMPLO por defecto: un único caso, usa solve()
    # -----------------------------------------------
    solve()

# ======================================================
#   Ejecución principal
# ======================================================
if __name__ == "__main__":
    main()
