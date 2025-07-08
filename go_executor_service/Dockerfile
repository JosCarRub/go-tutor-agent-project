FROM golang:1.24-alpine

WORKDIR /app

COPY . .


RUN go build -o go-executor-service .

EXPOSE 8090


ENTRYPOINT ["./go-executor-service"]