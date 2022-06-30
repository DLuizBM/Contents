import java.io.IOException;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner leitor = new Scanner(System.in);
        int N = leitor.nextInt();
        if (N > 1 && N < 1000) {
            for (int i = 1; i <= N; i++) {
                System.out.println(i + " " + (int) Math.pow(i, 2) + " " + (int) Math.pow(i, 3));
            }
        }
    }
}
