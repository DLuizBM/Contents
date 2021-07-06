package classeMetodo;

public class ValorReferencia103 {
	public static void main(String[] args) {
		double a = 2;
		double b = a; //atribuição por valor
		
		a++;
		b--;
	
		System.out.println(a + " " +  b);
		
		Data103 d1 = new Data103();
		Data103 d2 = d1;
		
		d1.dia = "01";
		d1.mes = "01";
		d1.ano = "1970";
		
		System.out.println(d1.dataFormatada());
		System.out.println(d2.dataFormatada());
		// as duas saída serão iguais, pois d2 aponta para o mesmo endereço
		// de memória de d1
		
		voltarDataPadrao(d1);
		// na chamada do método, será passado o objeto d1
		// mesmo tendo valores já definidos, no método o objeto ganha novos valores
		// com isso os valores em d2 também mudam, já que os 2 apontam para o mesmo
		// endereço de memória
		System.out.println(d1.dataFormatada());
		System.out.println(d2.dataFormatada());
		
		int c = 5;
		alterarPrimitivo(c);
		System.out.println(c);
		// nesse caso, o valor de c não muda, pois nos tipos primitivos os valores
		// são passados por valor, cria uma cópia,  e não referência
		// sendo assim, a variável a criada no método alterarPrimitivo, estará alocada em um local
		// totalmente diferente da variável c do main
		
	}
	// um método estático só consegue acessar outro método estático
	// um método estático não consegue acessar um método de instância
	// o que está sendo passado no método é um objeto do tipo Data103
	static void voltarDataPadrao(Data103 d) {
		d.dia = "01";
		d.mes = "08";
		d.ano = "1995";
	}
	
	static void alterarPrimitivo(int a) {
		a++;
	}
}
