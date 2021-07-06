package classeMetodo;

public class Desafio100 {

	static double desconto = 0.25;
	
	double precoComDesconto(double preco) {
		return preco * (1 - desconto);
	}
	double precoComDesconto(double preco, double descontoAdicional) {
		return preco * (1 - descontoAdicional);
	}
	
}
