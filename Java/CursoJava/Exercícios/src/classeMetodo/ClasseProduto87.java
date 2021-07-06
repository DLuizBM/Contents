package classeMetodo;

public class ClasseProduto87 {
	
	String nome;
	double preco;
	double desconto;
	
	double precoDesconto(double preco, double desconto) {
		double precoDesconto = 0;
		precoDesconto = preco - (preco * desconto);
		return precoDesconto;
	}
	
	double descontoDobrado() {
		return preco * (1 - 2 * desconto);
	}
	// como os atributos estão dentro da classe é possível fazer dessa forma
	// já que ao instanciar o produto na classe main, os atributos de preco
	// e desconto serão definidos
	double descontoDobrado(double descontoGerente) {
		return preco * (1 - 2 * desconto + descontoGerente);
	}
	// é possivel que haja métodos com o mesmo nome, mas com assinatura diferente
	// o JAVA sabe diferenciar os métodos, se na chamada estiver passando parâmetro
	// vai para o método em que há desconto de gerente, se não vai para o método
	// sem desconto de gerente
}
