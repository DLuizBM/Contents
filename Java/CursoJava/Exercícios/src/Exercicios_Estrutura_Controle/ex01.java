package Exercicios_Estrutura_Controle;

import java.util.Scanner;

public class ex01 {
	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		double number = input.nextDouble();
		
		if(0 < number && number < 10 && number % 2 == 0) {
			System.out.println("Yes, it is!!");
		}else {
			System.out.println("No, it is not!!");
		}
		
	}
}
