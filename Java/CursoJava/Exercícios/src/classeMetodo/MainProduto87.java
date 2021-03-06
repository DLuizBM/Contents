package classeMetodo;

import java.util.Scanner;

public class MainProduto87 {
	public static void main(String[] args) {
		/* como ClasseProduto87 está no mesmo pacote]
		 * não é necessário importar
		*/
		Scanner entrada = new Scanner(System.in);
		// Scanner é o tipo, a classe
		// new é a palavra reservada responsável por chamar o construtor
		// o nome do construtor tem exatamente o mesmo nome da classe
		// o primeiro Scanner é a classe, o segundo é o construtor
		entrada.close();
		
		ClasseProduto87 p1 = new ClasseProduto87();
		p1.nome = "notebook";
		p1.preco = 4500;
		p1.desconto = 0.1;
		
		// é possível fazer com var, pois o java vai inferir o tipo
		var p2 = new ClasseProduto87();
		p2.nome = "Ipad";
		p2.preco = 3499.99;
		p2.desconto = 0.12;
		
		System.out.println(p1.nome);
		System.out.println(p1.preco);
		System.out.println(p1.desconto);
		
		ClasseProduto87 desconto = new ClasseProduto87();
		
		System.out.println(desconto.precoDesconto(p1.preco, p1.desconto));
		System.out.println(p1.descontoDobrado());

	}
}
