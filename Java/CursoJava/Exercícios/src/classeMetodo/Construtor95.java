package classeMetodo;

public class Construtor95 {
	String nome;
	double preco;
	double desconto;
	
	// Definindo o construtor de forma explícita
	Construtor95(String nomeProduto) {
		// como o construtor exige um nome de produto
		// e para evitar que se passe o nome no construtor e pela notação ponto
		// na classe onde está se instanciando Construtor95 com a notação ponto
		// defini-se o String nome dentro do construtor
		nome = nomeProduto;
	}
	
	// Definindo o construtor padrão de forma explícita
	Construtor95(){
		
	}
	
	// Dessa forma é um método
	void COnstrutor95() {
		
	}
}
