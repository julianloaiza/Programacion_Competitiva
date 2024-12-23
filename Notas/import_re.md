Aquí tienes un resumen compacto del módulo **`re`** con sus funciones principales, definiciones y ejemplos. Este formato es ideal para usar como apunte.

---

# **Resumen del Módulo `re` en Python**

El módulo `re` permite trabajar con **expresiones regulares** para buscar, validar, extraer y manipular texto basado en patrones.

---

## **1. `re.match()`**
### **Definición**:
Verifica si el inicio de la cadena coincide con un patrón.

### **Ejemplo**:
```python
import re
texto = "Python es genial"
match = re.match(r'Python', texto)
print(bool(match))  # Salida: True
```

---

## **2. `re.search()`**
### **Definición**:
Busca el primer lugar donde el patrón aparece en la cadena.

### **Ejemplo**:
```python
import re
texto = "Mi número es 12345"
match = re.search(r'\d+', texto)  # Busca el primer número
print(match.group())  # Salida: 12345
```

---

## **3. `re.findall()`**
### **Definición**:
Encuentra todas las coincidencias en la cadena y las devuelve como una lista.

### **Ejemplo**:
```python
import re
texto = "Los números son 123 y 456"
numeros = re.findall(r'\d+', texto)  # Encuentra todos los números
print(numeros)  # Salida: ['123', '456']
```

---

## **4. `re.finditer()`**
### **Definición**:
Similar a `re.findall()`, pero devuelve un iterador con objetos `Match`.

### **Ejemplo**:
```python
import re
texto = "abc 123 xyz 456"
matches = re.finditer(r'\d+', texto)
for match in matches:
    print(match.group())  # Salida: 123, 456
```

---

## **5. `re.sub()`**
### **Definición**:
Reemplaza todas las coincidencias del patrón con un texto dado.

### **Ejemplo**:
```python
import re
texto = "Hola, mi número es 12345"
nuevo_texto = re.sub(r'\d+', 'XXXXX', texto)  # Reemplaza números por 'XXXXX'
print(nuevo_texto)  # Salida: Hola, mi número es XXXXX
```

---

## **6. `re.split()`**
### **Definición**:
Divide una cadena en partes usando un patrón como delimitador.

### **Ejemplo**:
```python
import re
texto = "uno,dos,tres,cuatro"
partes = re.split(r',', texto)  # Divide por comas
print(partes)  # Salida: ['uno', 'dos', 'tres', 'cuatro']
```

---

## **7. `re.compile()`**
### **Definición**:
Compila un patrón en un objeto reutilizable para búsquedas repetidas.

### **Ejemplo**:
```python
import re
patron = re.compile(r'\d+')
print(patron.findall("123 y 456"))  # Salida: ['123', '456']
```

---

## **8. `re.fullmatch()`**
### **Definición**:
Verifica si toda la cadena coincide exactamente con el patrón.

### **Ejemplo**:
```python
import re
texto = "12345"
es_valido = re.fullmatch(r'\d+', texto)
print(bool(es_valido))  # Salida: True
```

---

# **Metacaracteres y Sintaxis Común**

| **Metacarácter** | **Significado**              | **Ejemplo**                         |
|-------------------|------------------------------|--------------------------------------|
| `.`               | Cualquier carácter (excepto nueva línea) | `r'a.b'` coincide con "acb", "axb". |
| `^`               | Inicio de la cadena         | `r'^Hola'` coincide con "Hola mundo".|
| `$`               | Final de la cadena          | `r'mundo$'` coincide con "Hola mundo".|
| `*`               | 0 o más repeticiones        | `r'a*'` coincide con "", "a", "aaa". |
| `+`               | 1 o más repeticiones        | `r'a+'` coincide con "a", "aaa".    |
| `?`               | 0 o 1 repetición            | `r'a?'` coincide con "", "a".       |
| `{n}`             | Exactamente n repeticiones  | `r'a{3}'` coincide con "aaa".       |
| `{n,}`            | Al menos n repeticiones     | `r'a{2,}'` coincide con "aa", "aaa".|
| `{n,m}`           | Entre n y m repeticiones    | `r'a{2,4}'` coincide con "aa", "aaa".|
| `[]`              | Conjunto de caracteres      | `[aeiou]` coincide con "a", "e", etc.|
| `\d`              | Dígitos (`0-9`)             | `r'\d'` coincide con "1", "5", etc. |
| `\w`              | Alfanuméricos y guión bajo  | `r'\w'` coincide con "a", "9", etc. |
| `\s`              | Espacios en blanco          | `r'\s'` coincide con " ", "\t", etc.|

---

# **Ejemplo Completo**
```python
import re

texto = "Fecha: 31/12/2024, Precio: $40."

# Buscar una fecha
fecha = re.search(r'\d{2}/\d{2}/\d{4}', texto)
print("Fecha encontrada:", fecha.group())  # Salida: 31/12/2024

# Buscar precios
precio = re.search(r'\$\d+', texto)
print("Precio encontrado:", precio.group())  # Salida: $40

# Reemplazar números
nuevo_texto = re.sub(r'\d+', 'XXX', texto)
print("Texto modificado:", nuevo_texto)  # Salida: Fecha: XX/XX/XXXX, Precio: $XX.
```

---

### **Notas Finales**
- **`re`** es ideal para validar correos, extraer datos, limpiar texto o detectar patrones complejos.
- Usa herramientas como [regex101](https://regex101.com/) para probar y entender patrones.