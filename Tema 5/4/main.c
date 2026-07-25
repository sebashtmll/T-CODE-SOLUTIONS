#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include <sys/stat.h>

#ifdef _WIN32
#include <direct.h>
#mkdir(dir) _mkdir(dir)
#else
#define mkdir(dir) mkdir(dir, 0777)
#endif

// Función para generar archivos de prueba (5 < n < 20)
void generate_test_files(int count) {
    mkdir("test_docker_files");
    for (int i = 1; i <= count; i++) {
        char filename[100];
        sprintf(filename, "test_docker_files/docker-compose-%d.yml", i);
        FILE *f = fopen(filename, "w");
        if (!f) continue;

        fprintf(f, "version: '3.8'\n");
        fprintf(f, "services:\n");
        for (int j = 1; j <= i * 2; j++) {
            fprintf(f, "  app-%d:\n", j);
            fprintf(f, "    image: nginx:latest\n");
            fprintf(f, "    networks:\n");
            fprintf(f, "      net-uneg-%d:\n", j);
            fprintf(f, "        ipv4_address: 192.168.1.%d\n", 10 + j);
        }
        fprintf(f, "networks:\n");
        for (int j = 1; j <= i * 2; j++) {
            fprintf(f, "  net-uneg-%d:\n", j);
            fprintf(f, "    driver: bridge\n");
        }
        fclose(f);
    }
}

// Parser 1: Búsqueda lineal utilizando strstr
double measure_parser_strstr(const char *filepath) {
    clock_t start = clock();
    FILE *f = fopen(filepath, "r");
    if (!f) return 0.0;

    char line[256];
    while (fgets(line, sizeof(line), f)) {
        if (strstr(line, "ipv4_address:")) {
            // Simulación de extracción de token IP
            char *token = strchr(line, ':');
            if (token) {
                // Procesar valor tokenizado
                volatile char *ip = token + 1; 
                (void)ip;
            }
        }
    }
    fclose(f);
    clock_t end = clock();
    return ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0; // Milisegundos
}

// Parser 2: Parser basado en análisis de caracteres y delimitadores (Optimizado)
double measure_parser_custom_lexer(const char *filepath) {
    clock_t start = clock();
    FILE *f = fopen(filepath, "r");
    if (!f) return 0.0;

    char line[256];
    while (fgets(line, sizeof(line), f)) {
        // Omitir espacios iniciales de manera imperativa
        char *ptr = line;
        while (*ptr == ' ' || *ptr == '\t') ptr++;

        // Verificar prefijo exacto del token clave
        if (strncmp(ptr, "ipv4_address", 12) == 0) {
            char *val = strchr(ptr, ':');
            if (val) {
                val++;
                while (*val == ' ' || *val == '\t') val++;
                // Token detectado y aislado
                volatile char ip_char = *val;
                (void)ip_char;
            }
        }
    }
    fclose(f);
    clock_t end = clock();
    return ((double)(end - start) / CLOCKS_PER_SEC) * 1000.0;
}

int main() {
    int n_files = 10; // Rango válido: 5 < n < 20
    generate_test_files(n_files);

    printf("Iniciando pruebas de rendimiento en C con %d archivos...\n\n", n_files);
    printf("%-25s | %-20s | %-20s\n", "Archivo", "Parser Strstr (ms)", "Parser Custom (ms)");
    printf("--------------------------------------------------------------------------------\n");

    for (int i = 1; i <= n_files; i++) {
        char filepath[100];
        sprintf(filepath, "test_docker_files/docker-compose-%d.yml", i);

        double t1 = measure_parser_strstr(filepath);
        double t2 = measure_parser_custom_lexer(filepath);

        char filename_label[50];
        sprintf(filename_label, "docker-compose-%d.yml", i);
        printf("%-25s | %-20.4f | %-20.4f\n", filename_label, t1, t2);
    }

    return 0;
}