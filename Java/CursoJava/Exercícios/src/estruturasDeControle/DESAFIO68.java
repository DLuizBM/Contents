package estruturasDeControle;

import java.util.Scanner;

public class DESAFIO68 {
	public static void main(String [] args) {
		
		System.out.println("Digite a nota: ");
		Scanner entrada = new Scanner(System.in);
		
		int nota = 0;
		int total = 0;
		int contador = 0;
		
		nota = entrada.nextInt();
		
		while(nota != -1) {
			if(nota >= 0 && nota <= 10 ) {
				System.out.println("Nota válida!");
				total += nota;
				contador++;
			}else {
				System.out.println("Digite uma nota válida!");
			}
			System.out.println("Digite a nota: ");
			nota = entrada.nextInt();
		}
		System.out.printf("A média é: %d %d", total/contador, contador);
				
		entrada.close();
	}
}
