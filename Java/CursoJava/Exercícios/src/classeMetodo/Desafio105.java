package classeMetodo;

public class Desafio105 {
	
	int a = 5;
	// esse é um atributo que pertence a instancia
	static int b = 10;
	// algo estático pode acessar algo estático
	// dessa forma não será necessário fazer uma instância
	
	public static void main(String[] args) {
		// só é possível um método de classe acessar um atributo de instância
		// se for criado uma instância da classe, mesmo estando na própria classe
		
		Desafio105 var = new Desafio105();
		
		a();
		System.out.println(var.a);
		
		System.out.println(b);
		
	}
	// static void a() é um método de classe
	// ele conseguiu acessar a variável "a" quando foi feita a instância
	static void a() {
		Desafio105 a = new Desafio105();
		System.out.println(a.a);
	}

}
