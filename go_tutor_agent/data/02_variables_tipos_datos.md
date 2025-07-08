
---

### `leccion_02_variables_tipos_datos.md`

```markdown
# Lección 2: Variables, Constantes y Tipos de Datos Fundamentales

En la lección anterior, escribimos nuestro primer programa. Ahora, vamos a sumergirnos en cómo Go maneja los datos. Como lenguaje de tipado estático, Go es muy estricto pero claro sobre los tipos de datos que usas. Esto previene una gran cantidad de errores comunes en otros lenguajes.

## 1. Variables: Almacenando Información

Una variable es simplemente un nombre que le damos a una ubicación de memoria para almacenar un valor. En Go, hay varias formas de declarar una variable.

### Declaración Larga (Explícita)

Esta es la forma más verbosa pero también la más clara. Se usa la palabra clave `var`, seguida del nombre de la variable, su tipo y, opcionalmente, un valor inicial.

```go
// Declara una variable 'nombre' de tipo 'string'
var nombre string 

// Asigna un valor a la variable
nombre = "GoAgentTutor"

// También puedes declarar y asignar en la misma línea
var version float64 = 0.3
```

**¿Cuándo usarla?**
- Cuando necesitas declarar una variable a nivel de paquete (fuera de una función).
- Cuando quieres ser explícito sobre el tipo y el valor inicial (o su valor "cero").

### Valor Cero (Zero Value)

Si declaras una variable sin asignarle un valor inicial, Go automáticamente le asigna su "valor cero". Esto es una característica de seguridad importante que evita valores nulos o indefinidos inesperados.

- `0` para tipos numéricos (int, float).
- `false` para booleanos.
- `""` (una cadena vacía) para strings.

```go
var cantidad int     // cantidad es 0
var activo bool      // activo es false
var mensaje string   // mensaje es ""
```

### Declaración Corta (Implícita)

Dentro de las funciones, la forma más común y concisa de declarar e inicializar una variable es usando el operador de declaración corta `:=`.

```go
func miFuncion() {
    // El compilador infiere el tipo de la variable a partir del valor
    creador := "José Carlos Rubio" // Infiere que es de tipo string
    lecciones := 10               // Infiere que es de tipo int
    esGenial := true              // Infiere que es de tipo bool
}
```

**Reglas del Operador `:=`:**
1.  **Solo dentro de funciones:** No puedes usar `:=` fuera de una función (a nivel de paquete).
2.  **Declaración y asignación:** Siempre declara una nueva variable. No puedes usarlo para reasignar un valor a una variable ya existente. Para eso, usas el operador de asignación simple `=`.

```go
nombre := "Go" // OK: declara y asigna
nombre = "Golang" // OK: reasigna
// nombre := "Go v2" // ERROR: no new variables on left side of :=
```

## 2. Constantes: Valores Inmutables

Una constante es un valor que no puede cambiar una vez que ha sido declarado. Se declaran usando la palabra clave `const`.

```go
const Pi float64 = 3.14159265359
const Autor = "Google"
```

**Características de las Constantes:**
- Deben ser asignadas en el momento de la declaración.
- El valor debe ser conocido en tiempo de compilación (no puede ser el resultado de una llamada a una función, por ejemplo).
- Pueden ser "sin tipo" (untyped), lo que les da flexibilidad para ser usadas en diferentes contextos numéricos sin conversiones explícitas.

```go
const Año = 2024 // Constante sin tipo (puede ser int, int32, etc.)

var añoInt int = Año // Válido
var añoFloat float64 = Año // Válido
```

## 3. Tipos de Datos Fundamentales

Go viene con un conjunto de tipos de datos básicos que forman la base para construir estructuras más complejas.

### Tipos Enteros (Integers)

Go ofrece una variedad de tipos enteros, tanto con signo (`int`) como sin signo (`uint`). La elección depende del rango de valores que necesites almacenar.

- **Con signo:** `int8`, `int16`, `int32`, `int64`. El número indica los bits que usa.
- **Sin signo:** `uint8`, `uint16`, `uint32`, `uint64`. Solo almacenan números positivos.
- **Tipos genéricos:** `int` y `uint`. Su tamaño depende de la arquitectura del sistema (32 o 64 bits). **Generalmente, usarás `int` a menos que tengas una razón específica para no hacerlo.**

```go
var edad int = 30
var poblacionMundial uint64 = 8000000000
```

### Tipos de Punto Flotante (Floating-Point)

Se usan para números con decimales.

- `float32`: Precisión simple.
- `float64`: Precisión doble. **Es el tipo flotante recomendado y más común.**

```go
var precio float64 = 99.95
```

### Cadenas de Texto (Strings)

En Go, un `string` es una secuencia inmutable de bytes. Esto significa que una vez que creas una cadena, no puedes cambiar sus caracteres individuales.

```go
saludo := "Hola, Go!"
```

Puedes usar comillas dobles `"` para cadenas de una línea o acentos graves `` ` `` para cadenas multilínea (raw string literals), que también ignoran las secuencias de escape como `\n`.

```go
poema := `
La simplicidad es la clave,
en el código que fluye libre,
Go nos muestra el camino.
`
```

### Booleanos (Booleans)

Un tipo `bool` solo puede tener dos valores: `true` o `false`.

```go
var estaLloviendo bool = false
esViernes := true
```

## 4. Conversión de Tipos (Type Casting)

Go es muy estricto con los tipos. No puedes realizar operaciones entre variables de diferentes tipos sin una conversión explícita. Para convertir un valor a otro tipo, usas la sintaxis `Tipo(valor)`.

```go
var miEntero int = 42
var miFlotante float64 = 3.14

// Esto daría un error de compilación:
// resultado := miEntero + miFlotante 

// Esto es correcto:
resultado := float64(miEntero) + miFlotante // Convertimos el entero a float64
fmt.Println(resultado) // Salida: 45.14

// Convertir de flotante a entero trunca la parte decimal
var otroEntero int = int(miFlotante)
fmt.Println(otroEntero) // Salida: 3
```

## Resumen de la Lección

- **Variables:** Se declaran con `var` (explícita) o `:=` (corta, dentro de funciones).
- **Valor Cero:** Las variables no inicializadas tienen un valor predeterminado seguro (0, false, "").
- **Constantes:** Valores inmutables declarados con `const`.
- **Tipos Básicos:**
    - **Enteros:** `int` (el más común), `uint`, y sus variantes de tamaño específico.
    - **Flotantes:** `float64` (el más común), `float32`.
    - **Strings:** Inmutables, se definen con `"` o `` ` ``.
    - **Booleanos:** `bool` (`true` o `false`).
- **Conversión de Tipos:** Go requiere conversiones explícitas entre tipos usando la sintaxis `Tipo(valor)`.

**Próximos Pasos:** Ahora que sabemos cómo almacenar datos, en la siguiente lección aprenderemos a controlar el flujo de nuestro programa con **estructuras de control** como `if`, `else` y `for`.
```

---
