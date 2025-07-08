
---

### `leccion_08_interfaces.md`

```markdown
# Lección 8: Interfaces - Definiendo Comportamientos

En Go, una **interfaz** es un tipo que define un conjunto de métodos. En lugar de describir qué datos tiene un tipo (como un `struct`), una interfaz describe qué **comportamientos** tiene.

Si un tipo concreto (como un `struct`) implementa todos los métodos definidos en una interfaz, se dice que ese tipo "satisface" la interfaz. Esta es una de las características más poderosas de Go porque permite escribir funciones que operan sobre comportamientos, sin preocuparse por el tipo de dato exacto que están manejando.

## 1. Definiendo una Interfaz

Una interfaz se define con la palabra clave `type`, seguida del nombre de la interfaz y la palabra clave `interface`. Dentro, se listan las firmas de los métodos que la componen.

```go
package main

import (
    "fmt"
    "math"
)

// La interfaz 'Forma' define un comportamiento: cualquier tipo que sea una 'Forma'
// DEBE tener un método llamado 'area()' que devuelva un float64.
type Forma interface {
    area() float64
}
```

## 2. Implementación Implícita de Interfaces

Aquí es donde Go brilla y se diferencia de muchos otros lenguajes. En Go, **no declaras explícitamente que un tipo implementa una interfaz**. Simplemente, si tu tipo tiene todos los métodos que la interfaz requiere, automáticamente la satisface.

Vamos a crear dos tipos `struct` que satisfagan nuestra interfaz `Forma`.

```go
// Definimos un struct para un Rectángulo
type Rectangulo struct {
    ancho, alto float64
}

// Definimos un struct para un Círculo
type Circulo struct {
    radio float64
}

// Implementamos el método 'area()' para el tipo Rectangulo.
// Ahora, Rectangulo satisface la interfaz Forma.
func (r Rectangulo) area() float64 {
    return r.ancho * r.alto
}

// Implementamos el método 'area()' para el tipo Circulo.
// Ahora, Circulo también satisface la interfaz Forma.
func (c Circulo) area() float64 {
    return math.Pi * c.radio * c.radio
}
```

Tanto `Rectangulo` como `Circulo` tienen un método `area() float64`. Por lo tanto, ambos son considerados del tipo `Forma`.

## 3. Usando Interfaces para Escribir Código Genérico

Ahora podemos escribir una función que trabaje con cualquier `Forma`, sin importar si es un `Rectangulo`, un `Circulo` o cualquier otro tipo que definamos en el futuro que también tenga un método `area()`.

```go
// 'medir' es una función que acepta cualquier tipo que satisfaga la interfaz Forma.
func medir(f Forma) {
    fmt.Println("La forma recibida es:", f)
    fmt.Println("Su área es:", f.area())
}

func main() {
    r := Rectangulo{ancho: 10, alto: 5}
    c := Circulo{radio: 5}

    // Podemos pasar tanto un Rectangulo como un Círculo a la función 'medir',
    // porque ambos satisfacen la interfaz Forma.
    medir(r)
    fmt.Println("---")
    medir(c)
}
```

Salida del programa:
```
La forma recibida es: {10 5}
Su área es: 50
---
La forma recibida es: {5}
Su área es: 78.53981633974483
```

Este es el poder del polimorfismo en Go. La función `medir` no sabe ni le importa si está trabajando con un `Rectangulo` o un `Circulo`. Solo sabe que el valor que recibe tiene un método `area()`, y eso es todo lo que necesita.

## 4. La Interfaz Vacía: `interface{}` (o `any`)

Existe una interfaz especial llamada la **interfaz vacía**, que se escribe como `interface{}`. Como no tiene ningún método, **cualquier tipo en Go satisface la interfaz vacía**.

Esto significa que puedes crear funciones que acepten literalmente cualquier tipo de dato.

Desde Go 1.18, se introdujo un alias para `interface{}` que es más legible: `any`. Funcionalmente, son idénticos.

```go
func describir(i any) {
    fmt.Printf("El valor es '%v' y el tipo es '%T'\n", i, i)
}

func main() {
    describir(42)
    describir("hola")
    describir(true)
    describir(Rectangulo{ancho: 3, alto: 4})
}
```

Salida:
```
El valor es '42' y el tipo es 'int'
El valor es 'hola' y el tipo es 'string'
El valor es 'true' y el tipo es 'bool'
El valor es '{3 4}' y el tipo es 'main.Rectangulo'
```

**¿Cuándo usar `any`?**
Aunque parece muy flexible, debes usar `any` con precaución. Al aceptar cualquier tipo, pierdes la seguridad de tipos que el compilador te ofrece. Para saber qué tipo concreto se esconde detrás de una variable de tipo `any`, necesitas usar una "afirmación de tipo" (type assertion).

### Afirmaciones de Tipo (Type Assertions)

Una afirmación de tipo nos permite extraer el valor concreto de una variable de interfaz.

`valorConcreto := miVariableDeInterfaz.(TipoConcreto)`

Esto causará un `panic` (error fatal) si el tipo no es el correcto. Para manejarlo de forma segura, se usa la forma "coma, ok":

```go
func procesar(i any) {
    // Intentamos afirmar que 'i' es un string.
    s, ok := i.(string)
    if ok {
        fmt.Println("Es un string y su valor es:", s)
    } else {
        fmt.Println("No es un string.")
    }
}
```

También puedes usar un `switch` de tipos, que es una forma más elegante de manejar múltiples tipos posibles:

```go
func procesarConSwitch(i any) {
    switch v := i.(type) {
    case int:
        fmt.Printf("Es un entero y su valor es %d\n", v)
    case string:
        fmt.Printf("Es un string y su valor es '%s'\n", v)
    default:
        fmt.Printf("Tipo desconocido: %T\n", v)
    }
}
```

## Resumen de la Lección

- Una **interfaz** es un tipo que define un conjunto de **comportamientos** (firmas de métodos).
- La implementación de interfaces en Go es **implícita**: un tipo satisface una interfaz si tiene todos sus métodos.
- Las interfaces permiten escribir código **polimórfico y desacoplado**, que opera sobre comportamientos en lugar de tipos concretos.
- La **interfaz vacía** (`interface{}` o `any`) puede contener un valor de cualquier tipo.
- Las **afirmaciones de tipo** (`valor.(Tipo)`) se usan para recuperar el tipo concreto de una variable de interfaz.

**Próximos Pasos:** Hemos visto cómo definir contratos de comportamiento. Un comportamiento muy importante en cualquier programa es cómo manejar situaciones inesperadas. En la siguiente lección, exploraremos el enfoque idiomático de Go para el **manejo de errores**.
```

---
