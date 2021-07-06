package estruturasDeControle;

import java.util.Scanner;

public class DOWHILE67 {

	public static void main(String [] args) {
		
		Scanner entrada = new Scanner(System.in);
		String s = "";
		
		do {
			System.out.println("Fale " + "a palavra mágica");
			s = entrada.nextLine();
			
		} while(!s.equalsIgnoreCase("por favor"));
		
		entrada.close();
	}
}
