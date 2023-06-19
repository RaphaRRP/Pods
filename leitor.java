import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class leitor {

    public static void main(String[] args) {
        String csvFile = "convertido/dados.csv"; 

        try (BufferedReader br = new BufferedReader(new FileReader(csvFile))) {
            String line;
            boolean isFirstLine = true;
            String[] data = null;
            while ((line = br.readLine()) != null) {
                data = line.split(","); 
                if (isFirstLine) {
                    printHorizontalLine(data.length);
                    printRow(data);
                    printHorizontalLine(data.length);
                    isFirstLine = false;
                } else {
                    printRow(data);
                }
            }
            if (data != null) {
                printHorizontalLine(data.length);
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    private static void printRow(String[] data) {
        System.out.print("|");
        for (String value : data) {
            System.out.printf(" %-15s |", value); 
        }
        System.out.println();
    }

    private static void printHorizontalLine(int columns) {
        for (int i = 0; i < columns; i++) {
            System.out.print("+-----------------");
        }
        System.out.println("+");
    }
}