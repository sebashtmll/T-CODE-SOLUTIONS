import java.io.*;
import java.nio.file.*;
import java.util.regex.*;
import java.util.ArrayList;
import java.util.List;

public class DockerComposeBenchmark {

    public static void main(String[] args) {
        int nFiles = 10; // 5 < n < 20
        File testDir = new File("test_docker_files");
        if (!testDir.exists()) testDir.mkdir();

        // 1. Generar los archivos de prueba dinámicamente
        List<File> files = generateTestFiles(testDir, nFiles);

        System.out.println("Iniciando pruebas de rendimiento con " + nFiles + " archivos...\n");
        System.out.println(String.format("%-20s | %-15s | %-15s | %-15s", "Archivo", "Parser Regex (ms)", "Parser Manual (ms)", "Parser Estruct. (ms)"));
        System.out.println("----------------------------------------------------------------------------------");

        // 2. Ejecutar y medir cada parser
        for (File file : files) {
            long t1 = measureRegexParser(file);
            long t2 = measureManualParser(file);
            long t3 = measureStreamParser(file);

            System.out.println(String.format("%-20s | %-15d | %-15d | %-15d", file.getName(), t1, t2, t3));
        }
    }

    private static List<File> generateTestFiles(File dir, int count) {
        List<File> list = new ArrayList<>();
        for (int i = 1; i <= count; i++) {
            File f = new File(dir, "docker-compose-" + i + ".yml");
            try (PrintWriter pw = new PrintWriter(f)) {
                pw.println("version: '3.8'");
                pw.println("services:");
                for (int j = 1; j <= i * 2; j++) {
                    pw.println("  app-" + j + ":");
                    pw.println("    image: nginx:latest");
                    pw.println("    networks:");
                    pw.println("      net-uneg-" + j + ":");
                    pw.println("        ipv4_address: 192.168.1." + (10 + j));
                }
                pw.println("networks:");
                for (int j = 1; j <= i * 2; j++) {
                    pw.println("  net-uneg-" + j + ":");
                    pw.println("    driver: bridge");
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
            list.add(f);
        }
        return list;
    }

    // Parser 1: Basado en Expresiones Regulares
    private static long measureRegexParser(File file) {
        long start = System.nanoTime();
        try {
            String content = new String(Files.readAllBytes(file.toPath()));
            Pattern pattern = Pattern.compile("ipv4_address:\\s*(.+)");
            Matcher matcher = pattern.matcher(content);
            while (matcher.find()) {
                String ip = matcher.group(1).trim();
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return (System.nanoTime() - start) / 1_000_000; // Retorna en ms
    }

    // Parser 2: Lectura Manual Línea por Línea
    private static long measureManualParser(File file) {
        long start = System.nanoTime();
        try (BufferedReader br = new BufferedReader(new FileReader(file))) {
            String line;
            while ((line = br.readLine()) != null) {
                if (line.contains("ipv4_address:")) {
                    String[] parts = line.split(":");
                    if (parts.length > 1) {
                        String ip = parts[1].trim();
                    }
                }
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return (System.nanoTime() - start) / 1_000_000;
    }

    // Parser 3: Enfoque Estructural Ligero (Simulación de optimización custom)
    private static long measureStreamParser(File file) {
        long start = System.nanoTime();
        try {
            Files.lines(file.toPath())
                 .filter(line -> line.trim().startsWith("ipv4_address:"))
                 .map(line -> line.substring(line.indexOf(":") + 1).trim())
                 .forEach(ip -> {});
        } catch (IOException e) {
            e.printStackTrace();
        }
        return (System.nanoTime() - start) / 1_000_000;
    }
}