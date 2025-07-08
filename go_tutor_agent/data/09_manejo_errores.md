
---

### `leccion_09_manejo_de_errores.md`

```markdown
# Lección 9: Manejo de Errores en Go

El manejo de errores es una parte fundamental de la escritura de software robusto. Go aborda el manejo de errores de una manera muy particular y explícita, que difiere significativamente de las excepciones (`try/catch`) que se encuentran en lenguajes como Java, Python o C#.

En Go, los errores son simplemente **valores**.

## 1. El Enfoque de Go: Errores como Valores

La filosofía de Go es que los errores son una parte esperada del funcionamiento de un programa, no una situación excepcional. Por lo tanto, se manejan como cualquier otro valor.

Como vimos en la lección sobre funciones, es un patrón idiomático que una función que puede fallar devuelva dos valores: el resultado de la operación y un error.
- Si la operación es exitosa, el error devuelto es `nil`.
- Si la operación falla, se devuelve un valor de error que describe el problema.

El tipo `error` es en realidad una interfaz predefinida en Go. Cualquier tipo que implemente un método `Error() string` satisface la interfaz `error`.

```go
type error interface {
    Error() string
}
```

## 2. El Patrón `if err != nil`

El patrón más común que verás en el código Go para manejar errores es una comprobación explícita justo después de llamar a una función que puede fallar.

```go
package main

import (
    "fmt"
    "strconv" // Paquete para convertir strings a otros tipos
)

func main() {
    // strconv.Atoi convierte un string a un entero. Puede fallar.
    // Devuelve el entero y un error.
    numero, err := strconv.Atoi("123")
    
    // El patrón idiomático: comprobar si 'err' no es 'nil'.
    if err != nil {
        // Hubo un error. Lo manejamos aquí.
        // En un programa real, podrías registrar el error, mostrar un mensaje
        // amigable al usuario, o terminar el programa.
        fmt.Println("Ocurrió un error:", err)
        return // Salimos de la función main
    }

    // Si llegamos aquí, significa que err fue 'nil' y la conversión fue exitosa.
    fmt.Println("El número convertido es:", numero)


    // Veamos qué pasa con una entrada inválida
    numero, err = strconv.Atoi("no es un número")
    if err != nil {
        fmt.Println("Ocurrió un error:", err) // Esta vez, el error se imprimirá.
        return
    }

    fmt.Println("Este mensaje no se imprimirá.")
}
```

Este patrón, aunque puede parecer repetitivo, tiene grandes ventajas:
- **Claridad:** Hace que el flujo de control de errores sea explícito y fácil de seguir. No hay "saltos" inesperados como con las excepciones.
- **Robustez:** Obliga al programador a pensar en los errores en el punto exacto donde ocurren. Es más difícil ignorar un posible error.

## 3. Creando Errores Personalizados

Go proporciona dos formas sencillas de crear tus propios errores.

### Usando el Paquete `errors`

El paquete `errors` tiene una función `New()` que toma un string y devuelve un nuevo valor de error.

```go
import "errors"

func validarEdad(edad int) error {
    if edad < 0 {
        return errors.New("la edad no puede ser negativa")
    }
    if edad < 18 {
        return errors.New("el usuario debe ser mayor de edad")
    }
    return nil // No hay error
}
```

### Usando el Paquete `fmt`

El paquete `fmt` tiene una función `Errorf()` que funciona como `Printf`, pero devuelve un valor de error formateado. Esto es útil para incluir información dinámica en el mensaje de error.

```go
import "fmt"

func abrirArchivo(nombre string) error {
    // ... lógica para abrir el archivo ...
    // Supongamos que falla
    return fmt.Errorf("no se pudo abrir el archivo '%s'", nombre)
}
```

## 4. Tipos de Error Personalizados

A veces, un simple mensaje de error no es suficiente. Es posible que necesites un error que contenga más información estructurada, como un código de error o un timestamp.

Como `error` es una interfaz, puedes crear tu propio `struct` que la satisfaga.

```go
// Definimos un struct para nuestro error personalizado
type ErrorDeRed struct {
    Timestamp string
    Codigo    int
    Mensaje   string
}

// Implementamos el método Error() para que nuestro struct satisfaga la interfaz 'error'.
func (e *ErrorDeRed) Error() string {
    return fmt.Sprintf("en %s - código %d: %s", e.Timestamp, e.Codigo, e.Mensaje)
}

// Una función que devuelve nuestro error personalizado
func hacerPeticion() error {
    // ... lógica de la petición ...
    // Supongamos que falla
    return &ErrorDeRed{
        Timestamp: "2024-08-28T10:00:00Z",
        Codigo:    503,
        Mensaje:   "Servicio no disponible",
    }
}

func main() {
    err := hacerPeticion()
    if err != nil {
        fmt.Println(err)
    }
}
```

Con tipos de error personalizados, puedes usar afirmaciones de tipo (que vimos en la lección de interfaces) para comprobar el tipo específico del error y actuar en consecuencia.

## 5. `panic` y `recover`

Go tiene un mecanismo para manejar situaciones verdaderamente excepcionales e irrecuperables: `panic`.

Una llamada a `panic` detiene inmediatamente el flujo normal de ejecución. La función que llamó a `panic` se detiene, y la ejecución sube por la pila de llamadas (call stack), ejecutando cualquier sentencia `defer` que encuentre en el camino. Si no se controla, el programa se cierra y muestra el mensaje del `panic` y la pila de llamadas.

```go
func main() {
    panic("¡Algo salió terriblemente mal!")
    fmt.Println("Este mensaje nunca se mostrará.")
}
```

**¿Cuándo usar `panic`?**
Rara vez. `panic` está reservado para errores que indican un fallo de programación imposible de manejar, como un acceso a un índice fuera de los límites de un array o un puntero `nil` desreferenciado. **No debes usar `panic` para errores operacionales normales**, como no poder abrir un archivo o una conexión de red fallida. Para eso, usa el patrón de devolución de errores.

La función `recover` puede "atrapar" un `panic` dentro de una función `defer`, permitiendo que el programa recupere el control y continúe la ejecución, pero su uso es avanzado y poco común en la mayoría de las aplicaciones.

## Resumen de la Lección

- En Go, los **errores son valores** que se devuelven desde las funciones.
- El patrón idiomático es `if err != nil` para comprobar y manejar errores explícitamente.
- Puedes crear errores simples con `errors.New()` o `fmt.Errorf()`.
- Puedes crear **tipos de error personalizados** implementando la interfaz `error`.
- `panic` se usa para errores de programación irrecuperables, no para errores operacionales. El manejo de errores normal se hace devolviendo valores de tipo `error`.

**Próximos Pasos:** Hemos cubierto casi todos los fundamentos. En la última lección de esta serie, exploraremos la característica más célebre de Go: su increíblemente simple y potente modelo de **concurrencia** usando Goroutines y Canales.
```

---
