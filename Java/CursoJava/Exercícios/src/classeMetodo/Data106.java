package classeMetodo;

public class Data106 {
	
	// variáveis de instância
	int dia;
	int mes;
	int ano;
	static String decada;
	
	
	Data106(){
		//dia = 1;
		//mes = 1;
		//ano = 1970;
		
		// this pode ser usado para chamar um construtor a partir de outro construtor
		// aqui this é um método
		this(1, 1, 1970);
		// o que define qual construtor this está chamando é a quantidade de parâmetros
		// lembrando que java sabe qual chamar pelos parâmetros
		// não é possível chamar o this dessa forma, sem que seja dentro de um construtor
		// não pode ser chamado dentro de outro método, somente em construtores
	}
	
	Data106(int dia, int mes, int ano){
		// se fosse feiot
		// dia = dia;
		// nada seria feito, pois dia do lado esquerdo seria dia do lado direito
		// que vem no construtor, ou seja, não seria passado valor para int dia
		// declarado na linha 4.
		// com o this, o java sabe que this.dia é a variável da linha 4 e que dia depois de =
		// é o valor recebido no construtor.
		// ou seja, this aponta para o objeto atual que está executando o código
		
		// this(); chamando dentro desse construtor o this para o construtor padrão
		
		this.dia = dia;
		this.mes = mes;
		this.ano = ano;
	}
	// Método de instância
	// método de instância tem como acessar o this
	String dataFormatada() {
		decada = "2020";
		return dia+"/"+mes+"/"+this.ano;
	}
	
	void imprimirData() {
		System.out.println(this.dataFormatada());
	}
	// método estático não faz acesso ao this
	static void teste() {
		//this.dia = 3;
	}
	
}
