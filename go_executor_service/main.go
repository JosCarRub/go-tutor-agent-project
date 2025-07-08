package main

import (
	"encoding/json"
	"fmt"
	"log"
	"net/http"
	"os"
	"os/exec"
	"time"
)

type ExecuteRequest struct {
	Code string `json:"code"`
}

type ExecuteResponse struct {
	Output string `json:"output"`
	Error  string `json:"error"`
}

func executeHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodPost {
		http.Error(w, "Método no permitido", http.StatusMethodNotAllowed)
		return
	}

	var req ExecuteRequest
	if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
		http.Error(w, "Cuerpo de la petición inválido", http.StatusBadRequest)
		return
	}

	tempDir, err := os.MkdirTemp("", "goplayground")
	if err != nil {
		http.Error(w, "Error creando directorio temporal", http.StatusInternalServerError)
		return
	}
	defer os.RemoveAll(tempDir)

	goFilePath := fmt.Sprintf("%s/main.go", tempDir)
	if err := os.WriteFile(goFilePath, []byte(req.Code), 0644); err != nil {
		http.Error(w, "Error escribiendo en archivo temporal", http.StatusInternalServerError)
		return
	}

	initCmd := exec.Command("go", "mod", "init", "tempexec")
	initCmd.Dir = tempDir
	if err := initCmd.Run(); err != nil {
		log.Printf("Error al inicializar el módulo go: %v", err)
		http.Error(w, "Error interno del servidor al preparar el entorno de Go", http.StatusInternalServerError)
		return
	}

	binaryPath := fmt.Sprintf("%s/main", tempDir)
	buildCmd := exec.Command("go", "build", "-o", binaryPath, ".")
	buildCmd.Dir = tempDir
	buildOutput, err := buildCmd.CombinedOutput()
	if err != nil {
		log.Printf("Error de compilación de Go: %s", string(buildOutput))
		resp := ExecuteResponse{Error: string(buildOutput)}
		w.Header().Set("Content-Type", "application/json")
		json.NewEncoder(w).Encode(resp)
		return
	}

	if err := os.Chmod(binaryPath, 0755); err != nil {
		log.Printf("Error al añadir permisos de ejecución: %v", err)
		http.Error(w, "Error interno del servidor al preparar el ejecutable", http.StatusInternalServerError)
		return
	}

	runCmd := exec.Command(binaryPath)
	runOutput, err := runCmd.CombinedOutput()

	var resp ExecuteResponse
	if err != nil {
		resp.Error = string(runOutput)
	} else {
		resp.Output = string(runOutput)
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(resp)
}

func healthHandler(w http.ResponseWriter, r *http.Request) {
	w.WriteHeader(http.StatusOK)
	w.Write([]byte("OK"))
}

func main() {
	http.HandleFunc("/execute", executeHandler)
	http.HandleFunc("/health", healthHandler)

	port := os.Getenv("PORT")
	if port == "" {
		port = "8090"
	}

	server := &http.Server{
		Addr:         ":" + port,
		ReadTimeout:  10 * time.Second,
		WriteTimeout: 10 * time.Second,
	}
	log.Printf("Servidor Go Executor escuchando en el puerto %s", port)
	if err := server.ListenAndServe(); err != nil {
		log.Fatalf("No se pudo iniciar el servidor: %s\n", err)
	}
}
