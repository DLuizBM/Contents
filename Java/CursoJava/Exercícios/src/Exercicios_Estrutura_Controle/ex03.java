package Exercicios_Estrutura_Controle;

import java.util.Scanner;

public class ex03 {

	public static void main(String[] args) {
		
		double[] grades = new double[2];
		Scanner input = new Scanner(System.in);
		
		for(int i = 0; i < 2; i++) {
			double grade = input.nextDouble();
			grades[i] = grade;
		}
		
		double tot = 0;
		for(double grade: grades) {
			tot += grade;
		}
		System.out.println(tot/2);
		
		
	}
}
