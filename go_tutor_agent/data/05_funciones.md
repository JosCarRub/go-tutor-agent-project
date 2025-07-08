
---

### `leccion_05_funciones.md`

```markdown
# Lección 5: Funciones, los Bloques de Construcción del Código

Las funciones son el pilar fundamental para organizar el código en Go. Son bloques de código independientes y reutilizables que realizan una tarea específica. Al dividir un programa complejo en funciones más pequeñas y manejables, logramos que nuestro código sea más legible, fácil de mantener y de depurar.

## 1. Declaración Básica de una Función

Una función se declara con la palabra clave `func`, seguida del nombre de la función, una lista de parámetros entre paréntesis `()`, el tipo de valor de retorno y, finalmente, el cuerpo de la función entre llaves `{}`.

```go
package main

import "fmt"

// 'saludar' es una función que no toma parámetros y no devuelve ningún valor.
func saludar() {
    fmt.Println("¡Hola desde una función!")
}

// 'sumar' toma dos parámetros de tipo 'int' (a y b) y devuelve un valor de tipo 'int'.
func sumar(a int, b int) int {
    return a + b
}

func main() {
    // Llamamos a las funciones que hemos definido.
    saludar()

    resultado := sumar(5, 3)
    fmt.Println("El resultado de la suma es:", resultado) // Salida: 8
}
```

### Sintaxis Abreviada de Parámetros

Si varios parámetros consecutivos tienen el mismo tipo, puedes omitir el tipo en todos menos en el último.

```go
// En lugar de: func restar(a int, b int) int { ... }
// Podemos escribir:
func restar(a, b int) int {
    return a - b
}
```

## 2. Múltiples Valores de Retorno

Una de las características más poderosas y idiomáticas de Go es la capacidad de las funciones para devolver múltiples valores. Esto es extremadamente común para devolver un resultado y un posible error.

```go
import "errors"

// Esta función intenta dividir y devuelve el resultado (float64) y un error.
func dividir(a, b float64) (float64, error) {
    if b == 0 {
        // Si el divisor es cero, devolvemos el valor cero para float64 y un nuevo error.
        return 0, errors.New("no se puede dividir por cero")
    }
    // Si todo va bien, devolvemos el resultado y 'nil' para el error.
    return a / b, nil
}

func main() {
    // Usamos la forma "coma, ok" para capturar ambos valores de retorno.
    resultado, err := dividir(10.0, 2.0)
    if err != nil {
        // Hubo un error
        fmt.Println("Error:", err)
    } else {
        // No hubo error
        fmt.Println("Resultado de la división:", resultado)
    }

    resultado, err = dividir(10.0, 0.0)
    if err != nil {
        fmt.Println("Error:", err) // Se ejecutará esta parte
    } else {
        fmt.Println("Resultado de la división:", resultado)
    }
}
```

## 3. Valores de Retorno Nombrados (Named Return Values)

Go permite nombrar los valores de retorno en la firma de la función. Cuando se nombran, estas variables se inicializan con sus valores cero y están disponibles dentro de la función. Una sentencia `return` sin argumentos (un "naked return") devolverá los valores actuales de estas variables.

```go
// 'resultado' y 'resto' son valores de retorno nombrados.
func dividirConResto(dividendo, divisor int) (resultado, resto int) {
    if divisor == 0 {
        return // Devuelve los valores cero: 0, 0
    }
    resultado = dividendo / divisor
    resto = dividendo % divisor
    return // Devuelve los valores actuales de 'resultado' y 'resto'.
}

func main() {
    res, rem := dividirConResto(10, 3)
    fmt.Printf("Resultado: %d, Resto: %d\n", res, rem) // Salida: Resultado: 3, Resto: 1
}
```

**Advertencia:** Aunque los retornos nombrados pueden ser útiles en funciones cortas para mejorar la claridad, su uso excesivo, especialmente los "naked returns", puede hacer que el código sea más difícil de leer. Úsalos con moderación.

## 4. Funciones Variádicas

Una función variádica es aquella que puede aceptar un número variable de argumentos del mismo tipo. Esto se logra poniendo `...` antes del tipo del último parámetro.

Dentro de la función, el parámetro variádico se trata como un slice de ese tipo.

```go
// 'numeros' será un slice de tipo []int
func sumarTodo(numeros ...int) int {
    total := 0
    // Usamos un bucle for-range para iterar sobre el slice
    for _, numero := range numeros {
        total += numero
    }
    return total
}

func main() {
    fmt.Println(sumarTodo(1, 2))       // Salida: 3
    fmt.Println(sumarTodo(1, 2, 3, 4)) // Salida: 10

    // También puedes pasar un slice existente a una función variádica
    // usando la sintaxis '...' al final.
    miSlice := []int{5, 6, 7}
    fmt.Println(sumarTodo(miSlice...)) // Salida: 18
}
```

## 5. Funciones como Ciudadanos de Primera Clase

En Go, las funciones son "ciudadanos de primera clase". Esto significa que puedes tratar a las funciones como cualquier otro valor:
- Puedes asignarlas a variables.
- Puedes pasarlas como argumentos a otras funciones.
- Puedes hacer que una función devuelva otra función.

Esto abre la puerta a patrones de programación funcional muy potentes.

```go
func main() {
    // Asignar una función a una variable
    miOperacion := sumar

    fmt.Println(miOperacion(10, 20)) // Salida: 30

    // Pasar una función como argumento
    procesar(restar) // Salida: El resultado es: 7
}

// 'procesar' toma una función como argumento.
// El tipo de la función es 'func(int, int) int'
func procesar(operacion func(int, int) int) {
    resultado := operacion(10, 3)
    fmt.Println("El resultado es:", resultado)
}
```

### Funciones Anónimas (Closures)

También puedes definir funciones sobre la marcha sin darles un nombre. Estas se llaman funciones anónimas. A menudo se usan como *closures*, que son funciones que "recuerdan" el entorno en el que fueron creadas, permitiéndoles acceder a variables que están fuera de su propio cuerpo.

```go
func crearIncrementador() func() int {
    contador := 0
    return func() int {
        contador++
        return contador
    }
}

func main() {
    inc1 := crearIncrementador()
    fmt.Println(inc1()) // Salida: 1
    fmt.Println(inc1()) // Salida: 2

    inc2 := crearIncrementador() // inc2 tiene su propio 'contador'
    fmt.Println(inc2()) // Salida: 1
}
```

## Resumen de la Lección

- Las **funciones** se declaran con `func` y son la principal herramienta de organización de código.
- Pueden devolver **múltiples valores**, un patrón clave para el manejo de errores.
- Los **valores de retorno nombrados** pueden mejorar la claridad en funciones cortas.
- Las **funciones variádicas** (`...tipo`) aceptan un número variable de argumentos.
- Las funciones son **ciudadanos de primera clase**, lo que permite patrones de programación avanzados como pasarlas como argumentos o devolverlas desde otras funciones.

**Próximos Pasos:** Hemos aprendido a agrupar datos (slices, maps) y comportamiento (funciones). En la siguiente lección, combinaremos ambos conceptos para crear nuestros propios tipos de datos personalizados con comportamiento asociado usando **structs y métodos**.
```

---