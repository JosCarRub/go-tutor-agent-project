FROM maven:3.8.5-openjdk-17 AS builder

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos el pom.xml y el código fuente
COPY pom.xml .
COPY src ./src

# Construimos el proyecto. Maven usará el <finalName> del pom.xml
# para nombrar el JAR resultante como 'app.jar'.
RUN mvn clean package -DskipTests

# --- Etapa 2: Final ---
# Empezamos desde una imagen JRE slim.
FROM openjdk:17-slim

# Creamos un usuario sin privilegios para mayor seguridad.
RUN addgroup --system appgroup && adduser --system --group appuser

# Establecemos el directorio de trabajo
WORKDIR /app

# Copiamos el JAR con el nombre que hemos forzado en el pom.xml.
# Ya no hay ambigüedad ni necesidad de comodines.
COPY --from=builder /app/target/app.jar .

# Cambiamos al usuario sin privilegios.
USER appuser

# Exponemos el puerto de la aplicación.
EXPOSE 8080

# El comando para iniciar la aplicación.
ENTRYPOINT ["java", "-jar", "app.jar"]