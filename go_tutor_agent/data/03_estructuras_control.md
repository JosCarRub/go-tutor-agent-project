
---

### `leccion_03_estructuras_de_control.md`

```markdown
# Lección 3: Estructuras de Control (Decisiones y Bucles)

Los programas interesantes rara vez ejecutan una secuencia de instrucciones de principio a fin. Toman decisiones, reaccionan a diferentes entradas y repiten acciones. Las estructuras de control son las herramientas que nos permiten dictar este flujo lógico. En Go, la simplicidad es un principio rector, por lo que solo necesitarás dominar `if`, `switch` y `for`.

## 1. Condicionales: Tomando Decisiones

### La Sentencia `if / else`

La estructura `if` ejecuta un bloque de código solo si una condición es `true`.

Una característica distintiva de Go es que **no se usan paréntesis `()` alrededor de la condición**.

```go
package main

import "fmt"

func main() {
    edad := 19

    if edad >= 18 {
        fmt.Println("Eres mayor de edad.")
    }
}
```

Puedes añadir un bloque `else` para ejecutar código cuando la condición es `false`, y `else if` para encadenar múltiples condiciones.

```go
func main() {
    puntuacion := 75

    if puntuacion >= 90 {
        fmt.Println("Calificación: A")
    } else if puntuacion >= 80 {
        fmt.Println("Calificación: B")
    } else if puntuacion >= 70 {
        fmt.Println("Calificación: C")
    } else {
        fmt.Println("Calificación: F")
    }
}
```

#### `if` con una Sentencia de Inicialización

Go permite una forma idiomática y muy útil de la sentencia `if`: puedes ejecutar una sentencia corta de inicialización antes de la condición. La variable declarada en esta sentencia **solo existe dentro del alcance del bloque `if/else`**.

Esto es extremadamente común para manejar errores o verificar la existencia de valores.

```go
// Imagina una función que puede devolver un valor y un error
func obtenerDato() (string, bool) {
    // ...lógica para obtener un dato...
    return "Dato encontrado", true // o "", false si no se encuentra
}

func main() {
    // 'dato' y 'ok' solo existen aquí
    if dato, ok := obtenerDato(); ok {
        fmt.Println("Éxito:", dato)
    } else {
        fmt.Println("Fallo: No se pudo obtener el dato.")
    }

    // fmt.Println(dato) // ERROR: 'dato' no está definido aquí
}
```

### La Sentencia `switch`

La sentencia `switch` es una forma más limpia y legible de escribir una cadena de `if-else if`. Compara una expresión con una serie de valores (`case`).

```go
func main() {
    dia := "martes"

    switch dia {
    case "lunes":
        fmt.Println("¡Ánimo, empieza la semana!")
    case "martes":
        fmt.Println("Hoy es martes.")
    case "viernes":
        fmt.Println("¡Por fin es viernes!")
    default:
        fmt.Println("Es otro día de la semana.")
    }
}
```

**Características Clave del `switch` en Go:**
1.  **`break` Implícito:** A diferencia de lenguajes como C o Java, en Go no necesitas poner `break` al final de cada `case`. La ejecución sale del `switch` automáticamente. Si por alguna razón necesitas que la ejecución continúe al siguiente `case` (algo muy raro), puedes usar la palabra clave `fallthrough`.
2.  **Múltiples Valores por `case`:** Puedes agrupar varios valores en un solo `case` separándolos por comas.

    ```go
    switch dia {
    case "lunes", "martes", "miércoles", "jueves":
        fmt.Println("Día de trabajo.")
    case "sábado", "domingo":
        fmt.Println("¡Fin de semana!")
    }
    ```
3.  **`switch` sin Expresión:** Puedes usar `switch` sin una expresión, lo que lo convierte en una alternativa más limpia a una cadena `if-else if-else`.

    ```go
    puntuacion := 85
    switch {
    case puntuacion >= 90:
        fmt.Println("Excelente")
    case puntuacion >= 70:
        fmt.Println("Bueno")
    default:
        fmt.Println("Necesita mejorar")
    }
    ```

## 2. Bucles: Repitiendo Acciones

A diferencia de otros lenguajes que tienen múltiples tipos de bucles (`while`, `do-while`, `for`), Go simplifica todo con una única y versátil estructura de bucle: **`for`**.

### Forma 1: El Bucle `for` Clásico (Estilo C)

Esta es la forma más tradicional, con tres componentes separados por punto y coma: inicialización; condición; y post-ejecución.

`for inicialización; condición; post-ejecución { ... }`

```go
// Imprime los números del 0 al 4
for i := 0; i < 5; i++ {
    fmt.Println(i)
}
```

### Forma 2: El Bucle `for` como `while`

Puedes omitir la inicialización y la post-ejecución para que el `for` se comporte como un bucle `while` de otros lenguajes.

```go
suma := 1
for suma < 100 {
    suma += suma // Duplica la suma en cada iteración
}
fmt.Println(suma) // Imprimirá 128
```

### Forma 3: El Bucle Infinito

Si omites la condición por completo, creas un bucle infinito. Esto es útil para servidores que escuchan peticiones constantemente o cuando la condición de salida está dentro del bucle.

```go
for {
    fmt.Println("Este bucle se ejecutará para siempre...")
    // Necesitarías una sentencia 'break' o 'return' para salir.
}
```

### Forma 4: El Bucle `for-range` (para Colecciones)

Esta es una forma extremadamente útil y común para iterar sobre elementos de una colección como un array, slice, map o string. En cada iteración, devuelve el índice y el valor del elemento.

```go
nombres := []string{"Ana", "Juan", "Pedro"}

for indice, nombre := range nombres {
    fmt.Printf("Índice: %d, Nombre: %s\n", indice, nombre)
}
```

Si no necesitas el índice (o el valor), puedes usar el **identificador vacío `_`** para ignorarlo.

```go
// Ignorando el índice
for _, nombre := range nombres {
    fmt.Println("Nombre:", nombre)
}
```

## 3. Palabras Clave de Control de Bucles: `break` y `continue`

- **`break`**: Termina la ejecución del bucle `for` o `switch` más interno de forma inmediata.
- **`continue`**: Salta el resto del cuerpo del bucle en la iteración actual y pasa a la siguiente iteración.

```go
for i := 0; i < 10; i++ {
    if i == 5 {
        break // El bucle se detiene cuando i es 5
    }
    if i%2 != 0 {
        continue // Salta las iteraciones de números impares
    }
    fmt.Println(i) // Solo imprimirá 0, 2, 4
}
```

## Resumen de la Lección

- Las decisiones se toman con `if/else` (sin paréntesis) y `switch` (con `break` implícito).
- La repetición de tareas se maneja exclusivamente con el versátil bucle `for`, que puede actuar como un `for` clásico, un `while` o un iterador `for-range`.
- `break` y `continue` te dan control fino sobre la ejecución de los bucles.

**Próximos Pasos:** Ahora que sabemos cómo iterar, es el momento perfecto para aprender sobre las estructuras de datos que más comúnmente iteramos: los **tipos de datos compuestos** como arrays, slices y maps.
```

---