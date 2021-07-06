package classeMetodo;

import java.util.Scanner;

public class Main100 {
	public static void main(String[] args) {
		
		double preco = 0;
		double descontoAdicional = 0;
		
		Scanner entrada = new Scanner(System.in);
		
		preco = entrada.nextDouble();
		
		Desafio100 precoDesconto = new Desafio100();
		
		System.out.println(Desafio100.desconto);
		
		System.out.println(precoDesconto.precoComDesconto(preco));
		System.out.println(precoDesconto.precoComDesconto(preco, descontoAdicional));

		
		entrada.close();
	}
}
