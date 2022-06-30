package Lambdas;

public class main167 {
	
	public static void main(String[] args) {
		Calculo167 calculo = new Soma167();
		
		System.out.println(calculo.executar(2, 3));
		//System.out.println(calculo.somaDobrado(2, 3));
		
		calculo = new Multiplicar167();
		
		System.out.println(calculo.executar(2, 3));

		Soma167 somaTotal = new Soma167();
		System.out.println(somaTotal.executar(500,100));

		Soma167 somaDobrado = new Soma167();
		somaDobrado.somaDobrado(3, 4);


		/**
		 Os resultados das linhas 8 e 13 são diferentes, pois nesses instantes as intâncias
		 são diferentes. Na linha 8 a instância é de Soma167 e na linha 13 a instância é de
		 Multiplicar167. É possível usar o método executar nos 2 casos, pois a interface Calculo167
		 possui esse método e como ele está implementado nas 2 classes, o java consegue diferenciar
		 a forma de uso. É importante salientar que se o método executar não estivesse presente na interface
		 Calculo167, não seria possível usá-lo fazendo Calculo167 calculo = new Soma167() ou 
		 calculo = new Multiplicar167() .
		 Como exemplo, não se pode usar o método somaDobrado na linha 9, pois este não está definido na interface, e 
		 como se faz Calculo167 calculo = new Soma167(), está se instanciando uma Soma167(), mas o tipo será
		 Calculo167 e temos trabalhar de acordo com o tipo e não a instância, por isso, somente os métodos do
		 tipo que estarão disponíveis.
		*/
		
	}
}


