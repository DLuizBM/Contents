package Exercicios_Estrutura_Controle;

import java.util.Scanner;

public class ex02 {
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int year = input.nextInt();
		
		if(year % 4 == 0) {
			System.out.println("Bissexto!");
		}else {
			System.out.println("Não é bissexto!");
		}
		
	}
}
