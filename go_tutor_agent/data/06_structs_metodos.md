
---

### `leccion_06_structs_y_metodos.md`

```markdown
# Lección 6: Structs y Métodos - Creando Tipos Personalizados

Hasta ahora, hemos trabajado con los tipos de datos que Go nos proporciona. Pero el verdadero poder de un lenguaje de programación reside en la capacidad de crear nuestros propios tipos de datos complejos. En Go, la herramienta principal para esto es el **struct**.

## 1. ¿Qué es un Struct?

Un **struct** (abreviatura de "structure") es una colección de campos (fields) con nombre que nos permite agrupar datos relacionados en una sola unidad. Es como crear un plano o una plantilla para un nuevo tipo de dato.

Piensa en cómo describirías un "Usuario". Un usuario tiene un nombre, un email y una edad. Un struct nos permite definir exactamente eso.

### Declarando un Struct

Se declaran usando la palabra clave `type`, seguida del nombre del nuevo tipo y la palabra clave `struct`.

```go
package main

import "fmt"

// Definimos un nuevo tipo llamado 'Usuario'.
type Usuario struct {
    Nombre string
    Email  string
    Edad   int
    Activo bool
}

func main() {
    // ...
}
```
Hemos creado un nuevo tipo llamado `Usuario`. Ahora podemos crear variables (instancias) de este tipo.

### Creando Instancias de un Struct

Hay varias formas de crear una instancia de un struct:

```go
func main() {
    // 1. Forma explícita (valor cero)
    // Se crea un Usuario con los valores cero de sus campos ("", "", 0, false)
    var usuario1 Usuario
    usuario1.Nombre = "Ana"
    usuario1.Edad = 28
    fmt.Println("Usuario 1:", usuario1)

    // 2. Usando un literal de struct
    // Puedes especificar los valores de los campos por su nombre.
    usuario2 := Usuario{
        Nombre: "Juan",
        Email:  "juan@example.com",
        Edad:   35,
        Activo: true,
    }
    fmt.Println("Usuario 2:", usuario2)

    // 3. Forma corta del literal (¡Cuidado!)
    // Puedes omitir los nombres de los campos, pero DEBES proporcionar
    // todos los valores en el orden exacto en que se declararon.
    // No se recomienda porque es frágil; si añades un campo al struct, este código se romperá.
    usuario3 := Usuario{"Pedro", "pedro@example.com", 40, true}
    fmt.Println("Usuario 3:", usuario3)
}
```

### Accediendo a los Campos

Para acceder a los campos de una instancia de un struct, se utiliza el operador punto (`.`).

```go
fmt.Println("El email de Juan es:", usuario2.Email) // Salida: juan@example.com
```

## 2. Métodos: Añadiendo Comportamiento a los Structs

Un **método** es simplemente una función que tiene un "receptor" (receiver). El receptor vincula la función a un tipo específico, como nuestro struct `Usuario`. Esto nos permite añadir comportamiento a nuestros tipos de datos personalizados.

La sintaxis es similar a la de una función, pero se añade un parámetro receptor entre `func` y el nombre del método.

```go
// 'saludar' es un método del tipo 'Usuario'.
// '(u Usuario)' es el receptor.
// Dentro del método, 'u' se refiere a la instancia de Usuario sobre la que se llama el método.
func (u Usuario) saludar() {
    fmt.Printf("Hola, mi nombre es %s y tengo %d años.\n", u.Nombre, u.Edad)
}
```

Ahora podemos llamar a este método en cualquier instancia de `Usuario`:

```go
func main() {
    usuario := Usuario{Nombre: "Maria", Edad: 25}
    usuario.saludar() // Salida: Hola, mi nombre es Maria y tengo 25 años.
}
```

### Receptores de Puntero vs. Receptores de Valor

El receptor de un método puede ser de dos tipos:

1.  **Receptor de Valor (`func (u Usuario) ...`)**:
    - El método opera sobre una **copia** de la instancia del struct.
    - Cualquier modificación que hagas a `u` dentro del método **no afectará** a la instancia original.
    - Es la opción por defecto si el método no necesita modificar el struct.

2.  **Receptor de Puntero (`func (u *Usuario) ...`)**:
    - El método opera sobre un **puntero** a la instancia original del struct.
    - Cualquier modificación que hagas a los campos de `u` dentro del método **sí afectará** a la instancia original.
    - Es la opción necesaria cuando un método necesita modificar el estado del struct.
    - También es más eficiente para structs grandes, ya que evita copiar toda la estructura de datos cada vez que se llama al método.

Veamos un ejemplo de un método que modifica el struct:

```go
// Usamos un receptor de puntero (*Usuario) porque queremos modificar el campo 'Activo'.
func (u *Usuario) desactivar() {
    u.Activo = false
}

func main() {
    usuarioActivo := Usuario{
        Nombre: "Carlos",
        Activo: true,
    }
    fmt.Println("Antes de desactivar:", usuarioActivo.Activo) // Salida: true

    // Go es inteligente: aunque 'usuarioActivo' no es un puntero,
    // Go lo convierte automáticamente a un puntero para llamar al método.
    // Es decir, &usuarioActivo.desactivar() se llama implícitamente.
    usuarioActivo.desactivar()

    fmt.Println("Después de desactivar:", usuarioActivo.Activo) // Salida: false
}
```

**Regla general:** Si no estás seguro, usa un receptor de puntero. Es más versátil y a menudo más eficiente.

## 3. Structs Anidados y Campos Anónimos (Embedding)

Los structs pueden contener otros structs como campos.

```go
type Direccion struct {
    Calle string
    Ciudad string
}

type Persona struct {
    Nombre string
    Dir    Direccion // Un campo de tipo Direccion
}
```

Go también permite "incrustar" (embed) un struct dentro de otro. Esto se hace declarando un campo sin nombre, solo con el tipo. Los campos del struct incrustado se "promocionan" al struct contenedor, como si fueran suyos.

```go
type Contacto struct {
    Email string
    Telefono string
}

type Cliente struct {
    Nombre string
    Contacto // Campo anónimo (embedding)
}

func main() {
    cliente := Cliente{
        Nombre: "Empresa XYZ",
        Contacto: Contacto{
            Email: "contacto@xyz.com",
            Telefono: "123456789",
        },
    }

    // Podemos acceder a los campos de Contacto directamente desde cliente.
    fmt.Println(cliente.Email) // Salida: contacto@xyz.com
}
```
El embedding es la forma en que Go fomenta la **composición sobre la herencia**.

## Resumen de la Lección

- Los **structs** son la forma de crear tipos de datos personalizados en Go, agrupando campos con nombre.
- Los **métodos** son funciones vinculadas a un tipo (el receptor) que le añaden comportamiento.
- Los **receptores de puntero** (`*Tipo`) permiten a los métodos modificar la instancia original, mientras que los **receptores de valor** (`Tipo`) trabajan con una copia.
- El **embedding** (campos anónimos) es una forma de composición que permite que un struct "herede" los campos y métodos de otro.

**Próximos Pasos:** Hemos visto cómo crear tipos con datos y comportamiento. En la siguiente lección, exploraremos los **punteros** con más detalle para entender exactamente cómo Go maneja la memoria y por qué los receptores de puntero son tan importantes.
```

---
