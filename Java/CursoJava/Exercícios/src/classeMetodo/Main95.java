package classeMetodo;

public class Main95 {
	public static void main(String [] args) {
		Construtor95 produto = new Construtor95("Notebook");
		// como na classe Construtor95 o construtor foi definido de forma explícita
		// e ele exige uma string como parâmetro, ao declara o construtor aqui
		// deve-se passar a string.
		
		Construtor95 produto2 = new Construtor95();
		// utilizando o construtor padrão
		System.out.println(produto.nome);
	}
}
