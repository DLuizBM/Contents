package estruturasDeControle;

import java.util.Scanner;

public class While64 {
	public static void main(String[] args) {
		int contador = 0;
		while(contador <= 10) {
			if(contador != 1) {
				System.out.printf("contador = %d\n", contador);
			}
			contador++;
		}
		Scanner entrada = new Scanner(System.in);
		String s = entrada.nextLine();
		while(!s.equalsIgnoreCase("sair")) {
			System.out.println("Sair: ");
			s = entrada.nextLine();
		}
		entrada.close();
		
		
	}
}
