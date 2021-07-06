package estruturasDeControle;

import java.util.Scanner;

public class IF57 {
	public static void main(String [] args) {
		
		Scanner entrada = new Scanner(System.in);
		
		System.out.println("Informa a média: ");
		double media = entrada.nextDouble();
		
		if(media >= 7) {
			System.out.println("Parabéns");
		}
		
		entrada.close();
		
		double nota  = 1.3;
		if(nota >= 9.0) {
			System.out.println("Quadro de honra!!");
		}else {
			System.out.println("Reprovado!!");

		}
	}
}
