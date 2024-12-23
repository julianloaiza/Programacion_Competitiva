### **Clase: Sintaxis y Estructuras Básicas en Python**

---

### **1. Variables, Tipado Dinámico y Alcance de Variables**

#### **Variables y Tipado Dinámico**
- Python es de **tipado dinámico**, lo que significa que no necesitas declarar el tipo de la variable explícitamente.
- Puedes asignar valores y cambiar su tipo durante la ejecución.

**Ejemplo**:
```python
x = 10          # Entero
print(x, type(x))  # Salida: 10 <class 'int'>

x = "Hola"      # Cambia a cadena
print(x, type(x))  # Salida: Hola <class 'str'>

x = 3.14        # Cambia a flotante
print(x, type(x))  # Salida: 3.14 <class 'float'>
```

#### **Alcance de Variables**
- **Global**: Accesible desde cualquier parte del programa.
- **Local**: Declarada dentro de una función y accesible solo ahí.

**Ejemplo**:
```python
x = 5  # Variable global

def ejemplo():
    x = 10  # Variable local
    print("Dentro de la función:", x)

ejemplo()
print("Fuera de la función:", x)
```
**Salida**:
```
Dentro de la función: 10
Fuera de la función: 5
```

#### **Uso de `global`**
- Modifica una variable global dentro de una función.
```python
x = 5

def modificar_global():
    global x
    x = 10

modificar_global()
print(x)  # Salida: 10
```

---

### **2. Condicionales: `if/elif/else`**

- Las estructuras condicionales se usan para tomar decisiones basadas en condiciones.

**Ejemplo**:
```python
x = 10

if x > 5:
    print("x es mayor que 5")
elif x == 5:
    print("x es igual a 5")
else:
    print("x es menor que 5")
```

**Operadores comunes**:
- **Comparación**: `==`, `!=`, `<`, `>`, `<=`, `>=`
- **Lógicos**: `and`, `or`, `not`

**Ejemplo con operadores**:
```python
a, b = 10, 20

if a < b and b > 15:
    print("Ambas condiciones son verdaderas")
```

---

### **3. Bucles: `for` y `while`**

#### **Bucle `for`**
- Itera sobre elementos de una lista, rango, o cualquier objeto iterable.

**Ejemplo con `range`**:
```python
for i in range(5):  # Rango de 0 a 4
    print(i)
```

**Iterar sobre listas**:
```python
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)
```

#### **Bucle `while`**
- Se ejecuta mientras la condición sea verdadera.

**Ejemplo**:
```python
x = 0
while x < 5:
    print(x)
    x += 1
```

#### **Control de Bucles: `break` y `continue`**
- **`break`**: Termina el bucle.
- **`continue`**: Salta a la siguiente iteración.

**Ejemplo**:
```python
for i in range(10):
    if i == 5:
        break  # Detiene el bucle
    if i % 2 == 0:
        continue  # Salta los números pares
    print(i)
```

---

### **4. Definición de Funciones**

- Se definen con `def` y pueden tener parámetros con valores de retorno opcionales.

**Ejemplo básico**:
```python
def suma(a, b):
    return a + b

print(suma(3, 4))  # Salida: 7
```

#### **Argumentos por defecto**
- Asigna valores predeterminados a los parámetros.

**Ejemplo**:
```python
def saludar(nombre="Amigo"):
    print(f"Hola, {nombre}")

saludar()  # Salida: Hola, Amigo
saludar("Julián")  # Salida: Hola, Julián
```

#### **Argumentos variables**
- Usa `*args` para argumentos posicionales y `**kwargs` para argumentos nombrados.

**Ejemplo**:
```python
def mostrar(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

mostrar(1, 2, 3, nombre="Julián", edad=25)
```

**Salida**:
```
Args: (1, 2, 3)
Kwargs: {'nombre': 'Julián', 'edad': 25}
```

---

### **5. Estructuras de Datos Nativas**

#### **Listas (`list`)**
- Secuencias mutables.
```python
numeros = [1, 2, 3]
numeros.append(4)  # [1, 2, 3, 4]
numeros.pop()      # [1, 2, 3]
```

#### **Diccionarios (`dict`)**
- Pares clave-valor.
```python
dic = {"nombre": "Julián", "edad": 25}
print(dic["nombre"])  # Julián
dic["edad"] = 26
```

#### **Conjuntos (`set`)**
- Colección de elementos únicos.
```python
conjunto = {1, 2, 2, 3}
print(conjunto)  # {1, 2, 3}
```

#### **Tuplas (`tuple`)**
- Secuencias inmutables.
```python
tupla = (1, 2, 3)
print(tupla[0])  # 1
```

---

### **6. Manejo Básico de Excepciones**

- Usa `try` y `except` para manejar errores.

**Ejemplo**:
```python
try:
    resultado = 10 / 0
except ZeroDivisionError as e:
    print("Error:", e)
finally:
    print("Esto siempre se ejecuta")
```

**Salida**:
```
Error: division by zero
Esto siempre se ejecuta
```

---

### **Ejemplo Completo**

```python
def calcular_media(numeros):
    try:
        return sum(numeros) / len(numeros)
    except ZeroDivisionError:
        return "No se puede dividir por cero"
    except Exception as e:
        return f"Error inesperado: {e}"

if __name__ == "__main__":
    numeros = [1, 2, 3, 4]
    print("Media:", calcular_media(numeros))
```
