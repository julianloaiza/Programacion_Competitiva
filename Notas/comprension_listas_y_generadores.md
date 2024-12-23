# 1. Comprensiones de Listas (List Comprehensions)

## 1.1 ¿Qué son?
Las comprensiones de listas proporcionan una **sintaxis concisa** para crear nuevas listas a partir de iterables (listas, rangos, etc.).  
- Son a menudo **más rápidas** que construir la lista con un bucle `for` convencional en Python.  
- Permiten **anidar** y **filtrar** de forma muy compacta.

### Ejemplo básico

```python
# Crear una lista de cuadrados de 0 a 9
cuadrados = [x**2 for x in range(10)]
print(cuadrados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
```

### Anidamiento

```python
# Matriz 3x3 donde cada elemento es x*y
matriz = [[x * y for x in range(3)] for y in range(3)]
print(matriz)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

- Aquí se ve que anidamos dos comprensiones: la “interna” crea una lista en función de `x`, y la “externa” itera en `y`.

### Condicionales en Comprensiones

```python
# Obtener números pares en un rango
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # [0, 2, 4, 6, 8]
```

- Podemos poner el `if` al final para filtrar según la condición dada.

#### Uso en Competencias
1. **Lectura rápida**: Cuando obtienes un string con muchos números, puedes convertirlos rápidamente en enteros:
   ```python
   arr = [int(x) for x in input().split()]
   ```
2. **Filtrado rápido**: Para quedarte con los elementos que cumplen cierta condición:
   ```python
   positivos = [x for x in arr if x > 0]
   ```
3. **Transformaciones**: Para aplicar operaciones de forma compacta:
   ```python
   # Ejemplo: transformar coordenadas o pesos en una lista
   coordenadas = [(x+1, y+1) for (x, y) in coordenadas_originales]
   ```
4. **Mayor velocidad** que un bucle normal en la mayoría de los casos (aunque no siempre es significativo, en ciertos problemas de gran volumen de datos puede ayudar).

---

# 2. Generadores (Generators)

## 2.1 ¿Qué son?
Los generadores producen secuencias de valores **bajo demanda**, en vez de construir la lista completa en memoria.  
- **Ideal** cuando trabajas con **gran cantidad de datos** y no necesitas almacenarlos todos.  
- Se definen con la palabra reservada `yield` en una función, o usando **comprensión de generador** con paréntesis en lugar de corchetes.

### Ejemplo básico con `yield`

```python
def generador_cuadrados(n):
    for x in range(n):
        yield x**2

# Consumimos el generador
for valor in generador_cuadrados(5):
    print(valor)
# Imprime: 0 1 4 9 16
```

- Cada llamada a `yield` “devuelve” un valor sin perder el estado de la función.

### Comprensión de Generador

```python
gen = (x**2 for x in range(10))
print(next(gen))  # 0
print(next(gen))  # 1
```

- Usa **paréntesis** en lugar de corchetes (`[...]`) para construir un **generador** en vez de una lista.

## 2.2 Ventajas de los Generadores
- **Menor uso de memoria**: no guardan toda la lista, solo generan cada valor cuando se necesita.  
- **Evaluación diferida**: el cálculo del siguiente valor ocurre en el momento de la iteración, no por adelantado.  

| Aspecto             | Lista                      | Generador                   |
|---------------------|----------------------------|-----------------------------|
| **Memoria utilizada** | Alta (almacena todo)       | Baja (sólo guarda el estado)|
| **Evaluación**      | Inmediata (se crea la lista)| Diferida (bajo demanda)     |
| **Iteración**       | Sí                          | Sí                           |
| **Modificación posterior** | Sí (podemos añadir, etc.) | No (iteración única)         |

### Uso en Competencias
- Cuando solo **necesitas** iterar **una vez** sobre un conjunto enorme de datos para, por ejemplo, **sacar una suma o un mínimo/máximo**.  
- Ejemplo típico:  
  ```python
  # Sumar los cuadrados de números muy grandes sin crear listas enormes:
  numeros = map(int, input().split())  # ya es un iterador
  resultado = sum(x*x for x in numeros)
  ```
  Aquí, `sum(...)` consume el generador.

---

# 3. Ejemplo Comparativo

### Problema:
Dada una lista grande, encontrar la **suma de los cuadrados de todos los números pares**.

#### 3.1 Con Comprensión de Listas

```python
numeros = range(1, 10**6)
pares_cuadrados = [x**2 for x in numeros if x % 2 == 0]
print(sum(pares_cuadrados))
```

- Ventaja: sencillo y aún bastante rápido en Python.  
- Desventaja: crea una lista temporal de tamaño ~500,000 en memoria.

#### 3.2 Con Generador

```python
numeros = range(1, 10**6)
pares_cuadrados = (x**2 for x in numeros if x % 2 == 0)
print(sum(pares_cuadrados))
```

- No se almacena toda la lista, se va calculando y sumando sobre la marcha.  
- Si `10**6` fuera `10**8` (que es demasiado grande para Python en muchos casos competitivos), un generador te permite al menos no saturar memoria, aunque probablemente el tiempo de ejecución sea alto.

---

# 4. Consejos Prácticos de Optimización en Python

1. **Elegir la Estructura Correcta**  
   - `list` para manipular secuencias, pero si necesitas búsquedas e inserciones rápidas, prefiere `dict` o `set`.
   - `deque` (en `collections`) para colas, `pop/append` en ambos extremos en O(1).  

2. **Prefiere Generadores para Grandes Volúmenes**  
   - Si solo vas a **consumir** los datos **una vez** en un cálculo (ejemplo, `sum()`, `max()`, `min()`), usa un generador.  
   - Evitas gastar memoria construyendo listas inmensas.

3. **Minimiza Bucles Anidados**  
   - En competencias, el **cuello de botella** a menudo es un bucle O(n^2) o peor.  
   - Busca reestructurar el algoritmo para reducir la complejidad. A veces, un `set` para eliminar duplicados o una técnica “two pointers” pueden ayudarte a pasar de O(n^2) a O(n).

4. **Usa Funciones Integradas de Python**  
   - `sum(), min(), max(), sorted(), any(), all()` están optimizadas en C.  
   - `bisect` para búsqueda binaria en listas ordenadas.  
   - `itertools` para combinaciones, permutaciones, acumulados, etc.

### Ejemplo de comparación

```python
# Ineficiente: acumular con un bucle manual
total = 0
for x in range(100):
    total += x

# Más eficiente (internamente está optimizado en C):
total = sum(range(100))
```

5. **No abuses de la concatenación de Strings**  
   - Reemplaza ciclos de concatenación tipo `str1 += str2` con `join()` o un `list` + `''.join()`.  

6. **Si el Juez lo Permite**:  
   - **Pypy** puede ser más rápido en algunos algoritmos pesados que CPython.  
   - Aun así, la optimización principal se logra con un **buen algoritmo**.

---

# 5. Ejemplos Prácticos en Competencias

1. **Lectura de Datos Masivos**  
   ```python
   import sys
   data = sys.stdin.read().strip().split()  # Lee todo de golpe
   arr = (int(x) for x in data)  # Generador de enteros
   # Ejemplo: la suma total
   print(sum(arr))
   ```
   - Si el problema requiere la suma de miles o millones de valores, esto ahorra memoria frente a una gran lista.

2. **Filtrar y Contar**  
   ```python
   import sys
   n = int(sys.stdin.readline())
   valores = map(int, sys.stdin.readline().split())
   # Contar cuántos son pares
   pares = sum(1 for x in valores if x % 2 == 0)
   print(pares)
   ```
   - Aquí evitamos guardar todos los números; usamos un generador y `sum(...)` con una condición booleana.

3. **Uso de Comprensión para Preprocesar**  
   ```python
   # Tenemos n coordenadas en un plano
   n = int(input())
   coords = [tuple(map(int, input().split())) for _ in range(n)]
   # coords es una lista de tuplas (x, y)
   ```
   - Luego podemos operar sobre ellas. Más limpio y rápido que un bucle for clásico en Python.

4. **Optimizar Sumas**  
   ```python
   # Comparar
   # Opción A (bucle manual):
   s = 0
   for x in arr:
       s += x

   # Opción B (más conciso y usualmente más rápido):
   s = sum(arr)
   ```
   - En la mayoría de los casos, la **Opción B** es preferible.

---