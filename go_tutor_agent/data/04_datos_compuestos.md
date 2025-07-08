
---

Esta lección es fundamental, ya que los **slices** son una de las características más utilizadas y potentes del lenguaje. He puesto especial énfasis en diferenciar claramente entre arrays y slices, que es un punto clave para los recién llegados a Go.

### `leccion_04_tipos_de_datos_compuestos.md`

```markdown
# Lección 4: Tipos de Datos Compuestos (Arrays, Slices y Maps)

En Go, los tipos de datos compuestos nos permiten agrupar valores. Los tres tipos de colecciones más importantes que usarás a diario son los arrays, los slices y los maps. Entender sus diferencias y cuándo usar cada uno es crucial para escribir código idiomático y eficiente en Go.

## 1. Arrays: Colecciones de Tamaño Fijo

Un **array** es una secuencia numerada de elementos de un tipo específico con una **longitud fija**. Una vez que declaras un array de un tamaño determinado, no puedes cambiarlo.

La declaración de un array incluye su tamaño entre corchetes `[]`, seguido del tipo de sus elementos.

```go
package main

import "fmt"

func main() {
    // Declara un array 'primos' que contendrá 5 enteros.
    var primos [5]int 

    // Asignamos valores a sus posiciones (índices del 0 al 4)
    primos[0] = 2
    primos[1] = 3
    primos[2] = 5
    primos[3] = 7
    primos[4] = 11

    fmt.Println(primos) // Salida: [2 3 5 7 11]

    // También puedes declarar e inicializar en una sola línea
    nombres := [3]string{"Alice", "Bob", "Charlie"}
    fmt.Println(nombres) // Salida: [Alice Bob Charlie]
}
```

**Punto Clave:** El tamaño del array es parte de su tipo. Esto significa que `[5]int` y `[3]int` son tipos completamente diferentes. No puedes asignar uno al otro ni usarlos indistintamente.

**¿Cuándo usar arrays?**
Honestamente, en el código Go moderno, los arrays se usan con poca frecuencia directamente. Son la base sobre la que se construyen los slices, pero rara vez los manipularás tú mismo. Su uso principal es cuando necesitas una estructura de datos con un tamaño exacto y conocido en tiempo de compilación.

## 2. Slices: El Poder de la Flexibilidad

Un **slice** (rebanada) es la estructura de datos de colección más común y poderosa en Go. Piensa en un slice como una "vista" flexible y dinámica de un array subyacente. A diferencia de los arrays, los slices **no tienen un tamaño fijo**.

### Creando un Slice

La forma más común de crear un slice es usando la sintaxis de "literal de slice", que se parece a un literal de array pero sin el número en los corchetes.

```go
// Esto es un slice de strings, no un array.
letras := []string{"a", "b", "c", "d"}
fmt.Println(letras) // Salida: [a b c d]
```

### Propiedades de un Slice

Un slice tiene dos propiedades importantes:
- **Longitud (`len`)**: El número de elementos que contiene el slice.
- **Capacidad (`cap`)**: El número de elementos que el array subyacente puede contener, contando desde el primer elemento del slice.

```go
fmt.Println("Longitud:", len(letras)) // Salida: 4
fmt.Println("Capacidad:", cap(letras)) // Salida: 4
```

### La Función `make`

Para crear un slice con una longitud y capacidad iniciales, puedes usar la función `make`.

`make([]Tipo, longitud, capacidad)`

```go
// Crea un slice de enteros con longitud 5 y capacidad 10
numeros := make([]int, 5, 10)
fmt.Println(numeros)         // Salida: [0 0 0 0 0]
fmt.Println(len(numeros))    // Salida: 5
fmt.Println(cap(numeros))    // Salida: 10
```

### Añadiendo Elementos: `append`

La función `append` es la forma de añadir nuevos elementos a un slice. Devuelve un **nuevo slice** que contiene los elementos originales más los nuevos.

```go
var miSlice []int // Un slice "nil" (valor cero)
miSlice = append(miSlice, 10)
miSlice = append(miSlice, 20, 30)

fmt.Println(miSlice) // Salida: [10 20 30]
```

Si la capacidad del array subyacente no es suficiente, `append` creará un nuevo array más grande y copiará los elementos. Por eso es importante siempre asignar el resultado de `append` de nuevo a la variable del slice: `miSlice = append(miSlice, ...)`.

### "Rebanando" un Slice

Puedes crear nuevos slices a partir de uno existente usando la sintaxis `slice[inicio:fin]`.

```go
original := []string{"Lunes", "Martes", "Miércoles", "Jueves", "Viernes"}

// Crea un slice con los elementos desde el índice 1 hasta el 3 (sin incluir el 3)
diasDeSemana := original[1:3] // Contiene "Martes", "Miércoles"
fmt.Println(diasDeSemana)

// Puedes omitir el inicio o el fin
primerosDos := original[:2] // "Lunes", "Martes"
ultimosTres := original[2:] // "Miércoles", "Jueves", "Viernes"
```

**Importante:** Cuando creas una rebanada, el nuevo slice comparte el mismo array subyacente. Si modificas un elemento en la nueva rebanada, ¡el cambio se reflejará en el slice original!

## 3. Maps: Colecciones de Clave-Valor

Un **map** es una colección no ordenada de pares clave-valor. Es similar a los diccionarios en Python o los objetos en JavaScript. Son extremadamente útiles para búsquedas rápidas de datos.

La declaración de un map es: `map[TipoDeClave]TipoDeValor`.

### Creando un Map

Puedes usar `make` o un literal de map.

```go
// Usando make
edades := make(map[string]int)

// Asignando valores
edades["Alice"] = 30
edades["Bob"] = 25

fmt.Println(edades) // Salida: map[Alice:30 Bob:25]

// Usando un literal
puntuaciones := map[string]int{
    "matematicas": 95,
    "historia":    80,
}
fmt.Println(puntuaciones)
```

### Operaciones con Maps

- **Acceder a un valor:** `valor := miMap["clave"]`
- **Eliminar un par clave-valor:** `delete(miMap, "clave")`
- **Verificar si una clave existe:**
  Cuando accedes a una clave, un map puede devolver dos valores: el valor asociado a la clave y un booleano que es `true` si la clave existe.

```go
puntuacion, ok := puntuaciones["ciencias"]
if ok {
    fmt.Println("La puntuación de ciencias es:", puntuacion)
} else {
    fmt.Println("No hay puntuación para ciencias.")
}
```
Esta construcción de "coma, ok" es un modismo muy común en Go.

### Iterando sobre un Map

Puedes usar un bucle `for-range` para iterar sobre los pares clave-valor de un map. El orden de iteración no está garantizado.

```go
for materia, puntaje := range puntuaciones {
    fmt.Printf("Materia: %s, Puntaje: %d\n", materia, puntaje)
}
```

## Resumen de la Lección

- **Arrays**: Colecciones de tamaño **fijo**. Su tamaño es parte de su tipo. Rara vez se usan directamente.
- **Slices**: Colecciones **dinámicas y flexibles** que apuntan a un array subyacente. Son el tipo de colección secuencial más usado en Go. Se modifican con `append`.
- **Maps**: Colecciones **no ordenadas** de pares clave-valor. Optimizados para búsquedas rápidas.

**Próximos Pasos:** Ahora que podemos agrupar datos, el siguiente paso es aprender a agrupar comportamiento. En la próxima lección, exploraremos las **funciones**, que nos permiten organizar nuestro código en bloques reutilizables.
```

---
