package Lambdas;

public class main167 {
	
	public static void main(String[] args) {
		Calculo167 calculo = new Soma167();
		
		System.out.println(calculo.executar(2, 3));
		
		calculo = new Multiplicar167();
		
		System.out.println(calculo.executar(2, 3));

		Soma167 somaTotal = new Soma167();
		System.out.println(somaTotal.executar(500,100));
		
	}
}


