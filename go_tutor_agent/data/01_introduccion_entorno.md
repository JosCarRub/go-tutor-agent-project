
---

### `leccion_01_introduccion_y_entorno.md`

```markdown
# Lección 1: Introducción a Go y Configuración del Entorno

¡Bienvenido al fascinante mundo de Go! Antes de sumergirnos en el código, es crucial entender qué es Go, por qué fue creado y cómo preparar tu máquina para empezar a programar.

## 1. ¿Qué es Go? (El "Porqué")

Go, a menudo llamado Golang, es un lenguaje de programación de código abierto creado en Google en 2009 por Robert Griesemer, Rob Pike y Ken Thompson. Estos son algunos de los mismos ingenieros que crearon el sistema operativo Unix y el lenguaje de programación C, ¡así que sabían lo que hacían!

Go fue diseñado para resolver problemas del mundo real que Google enfrentaba a gran escala:
- **Compilaciones lentas:** Lenguajes como C++ tardaban horas en compilar en los sistemas masivos de Google.
- **Gestión de dependencias complicada:** Manejar las librerías de las que dependía un proyecto era un caos.
- **Dificultad con la concurrencia:** Aprovechar los procesadores multinúcleo modernos era complejo y propenso a errores.

Piensa en Go como una navaja suiza para el desarrollo de software moderno: simple, increíblemente rápido y diseñado desde cero para la concurrencia.

### Características Principales

- **Simplicidad:** Go tiene una sintaxis limpia y concisa con un número muy reducido de palabras clave (solo 25). Esto hace que sea fácil de aprender y leer.
- **Concurrencia nativa:** Go facilita la creación de programas que hacen múltiples cosas a la vez a través de **Goroutines** y **Canales (Channels)**. Esto es una de sus características más potentes.
- **Rendimiento excepcional:** Go es un lenguaje compilado. Se compila directamente a código máquina, lo que resulta en binarios ejecutables muy rápidos, con un rendimiento cercano al de C o C++.
- **Tipado estático y seguro:** Las variables deben tener un tipo definido, lo que permite al compilador detectar muchos errores antes de que el programa se ejecute.
- **Ecosistema robusto:** Viene con una biblioteca estándar muy completa y herramientas de desarrollo integradas que simplifican tareas como el testing, el formateo de código y la gestión de paquetes.

## 2. ¿Por qué aprender Go hoy?

Go no es solo un proyecto de Google; es el lenguaje que impulsa gran parte de la infraestructura de la nube. Proyectos como **Docker**, **Kubernetes**, **Prometheus** y **Terraform** están escritos en Go. Empresas como Dropbox, Uber, Twitch y, por supuesto, Google, lo utilizan extensivamente para sus servicios de backend.

Aprender Go te abre las puertas al desarrollo de:
- APIs y microservicios de alto rendimiento.
- Herramientas de línea de comandos (CLI).
- Sistemas distribuidos y de redes.
- Herramientas de DevOps y automatización.

## 3. Instalación y Configuración del Entorno

¡Suficiente teoría! Vamos a preparar tu entorno.

### Paso 1: Descargar e Instalar Go

1.  Ve a la página oficial de descargas de Go: **[go.dev/dl/](https://go.dev/dl/)**
2.  Descarga el instalador para tu sistema operativo (Windows, macOS o Linux).
3.  Ejecuta el instalador. Generalmente, se encarga de todo, incluyendo la configuración de las variables de entorno necesarias como `PATH`.

### Paso 2: Verificar la Instalación

Abre una terminal o línea de comandos y ejecuta el siguiente comando:

```bash
go version
```

Deberías ver una salida similar a esta (la versión puede variar):
`go version go1.22.5 darwin/arm64`

Si ves esto, ¡felicidades! Go está instalado correctamente.

### Paso 3: Entendiendo el Espacio de Trabajo Moderno (Go Modules)

Antiguamente, Go usaba un sistema llamado `GOPATH` que obligaba a tener todo tu código en un solo lugar. Hoy en día, el estándar es usar **Go Modules**, que te permite crear proyectos en cualquier carpeta de tu ordenador.

Un "módulo" es simplemente una colección de paquetes de Go que se versionan juntos. Es la forma moderna y recomendada de gestionar las dependencias de tu proyecto.

## 4. Creando tu Primer Proyecto con Go Modules

Vamos a crear nuestro primer proyecto.

1.  **Crea una carpeta para tu proyecto:**
    ```bash
    mkdir mi-primer-proyecto
    cd mi-primer-proyecto
    ```

2.  **Inicializa el módulo:**
    ```bash
    go mod init mi-primer-proyecto
    ```
    Este comando crea un archivo llamado `go.mod`. Este archivo rastreará las dependencias de tu proyecto. Por ahora, solo contendrá el nombre del módulo.

3.  **Crea tu primer archivo Go:**
    Crea un archivo llamado `main.go` dentro de la carpeta `mi-primer-proyecto`.

### ¡Hola, Mundo! - Tu Primer Programa

Abre `main.go` en tu editor de código favorito y escribe lo siguiente:

```go
package main

import "fmt"

func main() {
    fmt.Println("¡Hola, Mundo desde Go!")
}
```

#### Desglose del Código:
- `package main`: Declara que este archivo pertenece al paquete `main`. El paquete `main` es especial: le dice a Go que este programa es un ejecutable (algo que puedes correr), no una librería.
- `import "fmt"`: Importa el paquete `fmt` (abreviatura de "format"). Este paquete contiene funciones para formatear e imprimir texto, como `Println`.
- `func main()`: Define la función `main`. Esta es la puerta de entrada de tu programa. Cuando ejecutas el programa, el código dentro de esta función es lo primero que se ejecuta.
- `fmt.Println(...)`: Llama a la función `Println` del paquete `fmt` para imprimir una línea de texto en la consola.

## 5. Compilar y Ejecutar

Hay dos formas principales de ejecutar tu programa:

1.  **Ejecución directa (`go run`):**
    Este comando compila y ejecuta tu programa en un solo paso. Es ideal para el desarrollo rápido.
    ```bash
    go run main.go
    ```
    Verás la salida: `¡Hola, Mundo desde Go!`

2.  **Compilación (`go build`):**
    Este comando compila tu código y crea un archivo ejecutable binario.
    ```bash
    go build
    ```
    Si miras en tu carpeta, ahora tendrás un nuevo archivo llamado `mi-primer-proyecto` (o `mi-primer-proyecto.exe` en Windows). Puedes ejecutarlo directamente:
    ```bash
    ./mi-primer-proyecto
    ```
    La salida será la misma. La ventaja es que este archivo binario es autocontenido y puedes distribuirlo y ejecutarlo en cualquier máquina con el mismo sistema operativo sin necesidad de tener Go instalado.

## Resumen de la Lección

- **Go es un lenguaje simple, rápido y compilado**, diseñado para la eficiencia y la concurrencia.
- Es muy relevante hoy en día, especialmente en el **desarrollo de backend y DevOps**.
- La instalación es sencilla a través de **go.dev**.
- Los proyectos modernos se gestionan con **Go Modules** (`go mod init`).
- Un programa ejecutable debe tener un `package main` y una `func main()`.
- Puedes ejecutar código rápidamente con `go run` o crear un ejecutable con `go build`.

¡Felicidades! Has configurado tu entorno y ejecutado tu primer programa en Go. Estás listo para el siguiente paso.

**Próximos Pasos:** En la siguiente lección, exploraremos en profundidad las **variables y los tipos de datos básicos** en Go.
```

---
