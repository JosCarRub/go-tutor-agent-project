
---

### `leccion_10_concurrencia.md`

```markdown
# Lección 10: Concurrencia en Go (Goroutines y Canales)

La concurrencia es la capacidad de un programa para ejecutar múltiples tareas de forma independiente y, a menudo, simultáneamente. En el mundo de los procesadores multinúcleo, la concurrencia es clave para el rendimiento. Go fue diseñado desde cero con la concurrencia como una característica central, haciéndola sorprendentemente fácil de implementar.

La filosofía de Go sobre la concurrencia se resume en este famoso lema:
> "No te comuniques compartiendo memoria; en su lugar, comparte memoria comunicándote."

Esto se logra a través de dos mecanismos principales: **Goroutines** y **Canales (Channels)**.

## 1. Goroutines: Hilos de Ejecución Ligeros

Una **Goroutine** es una función que se ejecuta de forma concurrente junto con otras Goroutines en el mismo espacio de direcciones. Piensa en ellas como hilos de ejecución extremadamente ligeros, gestionados por el propio runtime de Go, no directamente por el sistema operativo.

Crear una Goroutine es increíblemente simple: solo tienes que anteponer la palabra clave `go` a una llamada de función.

```go
package main

import (
    "fmt"
    "time"
)

func decir(texto string) {
    for i := 0; i < 5; i++ {
        time.Sleep(100 * time.Millisecond) // Pausa para ver el efecto
        fmt.Println(texto)
    }
}

func main() {
    // Inicia una nueva Goroutine que ejecuta la función 'decir'.
    // El programa NO espera a que termine.
    go decir("mundo")

    // La función 'main' continúa su ejecución en su propia Goroutine.
    decir("hola")
}
```

Si ejecutas este código, verás una salida como esta (el orden puede variar):
```
hola
mundo
hola
mundo
hola
mundo
hola
mundo
hola
mundo
```
Las palabras "hola" y "mundo" se imprimen de forma intercalada, demostrando que ambas funciones se estaban ejecutando al mismo tiempo.

**Un problema común:** ¿Qué pasa si la Goroutine `main` termina antes que las otras?

```go
func main() {
    go decir("adiós") // Esta Goroutine empieza...
    
    // ...pero la función main termina inmediatamente.
    // El programa se cierra y la Goroutine 'decir' probablemente no tenga tiempo de ejecutarse.
}
```
Para solucionar esto, necesitamos una forma de que las Goroutines se comuniquen y sincronicen. Y para eso están los canales.

## 2. Canales (Channels): Comunicando Goroutines

Un **canal** es una tubería tipada a través de la cual puedes enviar y recibir valores entre Goroutines. Son la forma idiomática y segura de compartir datos.

### Creando un Canal

Se crean con la función `make`, especificando el tipo de dato que transportarán.

```go
// Crea un canal que transportará valores de tipo string.
mensajes := make(chan string)
```

### Enviando y Recibiendo Datos

- **Enviar un valor a un canal:** `canal <- valor`
- **Recibir un valor de un canal:** `variable := <-canal`

El envío y la recepción de datos en un canal son operaciones **bloqueantes**.
- Cuando envías un valor, la Goroutine se pausa hasta que otra Goroutine esté lista para recibirlo.
- Cuando intentas recibir un valor, la Goroutine se pausa hasta que otra Goroutine envíe un valor a ese canal.

Este comportamiento bloqueante es la clave de la sincronización en Go.

### Ejemplo de Sincronización con Canales

Vamos a usar un canal para asegurarnos de que nuestra Goroutine `main` espere a que otra termine.

```go
func trabajador(terminado chan bool) {
    fmt.Println("Trabajando...")
    time.Sleep(time.Second) // Simula un trabajo
    fmt.Println("¡Terminado!")

    // Envía un valor booleano al canal para señalar que ha finalizado.
    terminado <- true
}

func main() {
    // Creamos un canal para la señal de finalización.
    canalTerminado := make(chan bool)

    // Iniciamos el trabajador en una nueva Goroutine, pasándole el canal.
    go trabajador(canalTerminado)

    // La Goroutine 'main' se bloquea aquí, esperando recibir un valor
    // del canal 'canalTerminado'. No continuará hasta que eso ocurra.
    <-canalTerminado

    fmt.Println("La Goroutine principal ha recibido la señal y ahora puede terminar.")
}
```

## 3. Canales con Búfer (Buffered Channels)

Por defecto, los canales no tienen búfer. Esto significa que solo aceptan un envío si hay un receptor listo.

Puedes crear un canal con un búfer para permitir que se almacenen un número limitado de valores sin un receptor correspondiente.

`canalConBuffer := make(chan int, 2) // Puede almacenar 2 enteros`

Los envíos a un canal con búfer solo se bloquean si el búfer está lleno. Las recepciones solo se bloquean si el búfer está vacío.

```go
func main() {
    mensajes := make(chan string, 2)

    // Podemos enviar dos valores sin que nadie los reciba, porque el búfer tiene capacidad 2.
    mensajes <- "hola"
    mensajes <- "mundo"

    // Si intentáramos enviar un tercero, el programa se bloquearía (deadlock).
    // mensajes <- "extra" 

    fmt.Println(<-mensajes)
    fmt.Println(<-mensajes)
}
```

## 4. Iterando sobre Canales con `for-range`

Puedes usar un bucle `for-range` para recibir valores de un canal hasta que este sea **cerrado**.

```go
func productor(c chan int) {
    for i := 0; i < 5; i++ {
        c <- i // Envía los números del 0 al 4
    }
    close(c) // ¡Importante! Cierra el canal para señalar que no se enviarán más valores.
}

func main() {
    miCanal := make(chan int)
    go productor(miCanal)

    // El bucle for-range recibe valores del canal hasta que se cierra.
    for numero := range miCanal {
        fmt.Println(numero)
    }
}
```

Solo el **emisor** debe cerrar un canal, nunca el receptor. Enviar a un canal cerrado causará un `panic`.

## Resumen de la Lección

- La **concurrencia** en Go se basa en **Goroutines** y **Canales**.
- Una **Goroutine** es una función que se ejecuta concurrentemente. Se inicia con la palabra clave `go`.
- Un **Canal** es una tubería para comunicar Goroutines de forma segura. Se crean con `make(chan Tipo)`.
- El envío (`<-`) y la recepción (`<-`) en canales son operaciones **bloqueantes** que permiten la sincronización.
- Los **canales con búfer** permiten almacenar un número limitado de valores.
- Se puede iterar sobre un canal con `for-range` hasta que el emisor lo **cierre** con `close()`.

¡Felicidades! Has completado los fundamentos de Go. Con estos 10 conceptos, tienes una base sólida para empezar a construir aplicaciones reales y explorar el vasto ecosistema de Go.
```

---

