package Exercicios_Estrutura_Controle;

import java.util.Random;
import java.util.Scanner;

public class ex06 {

	public static void main(String[] args) {
		
		Scanner input = new Scanner(System.in);
		int num;
		Random rand = new Random();
		int numRand = rand.nextInt(1000) + 1;
		System.out.println(numRand);
		num = input.nextInt();
		int i = 0;
		while(num != numRand && i < 10) {
			System.out.println("Wrong number!");
			if(num < numRand) {
				System.out.println("Bigger");
			}else {
				System.out.println("Smaller");
			}
			num = input.nextInt();
			i++;
		}
		
	}
}
