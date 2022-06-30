package Lambdas;

public class mainLambda {

	public static void main(String[] args) {
		
		Calculo167 calculo = (x, y) -> {
			return x + y;
		};
		// o conceito de lambdas é similar ao das arrow functions em JS
		// aqui o java sabe, pelo tipo de instância (Calculo167), que 
		// dentro da interface tem um método que espera receber dois parâmetros,
		// assim sendo, ele sabe de que função da interface estamos implementando
		
		System.out.println(calculo.executar(3, 2));
		
		// outra forma de usar, dessa maneira o retorno é implícito
		calculo = (x, y) -> x * y;
		System.out.println(calculo.executar(2, 3));

		Calculo167 calc = new Soma167();
		System.out.println(calc.executar(3, 2));
		// O método executar aqui vai ter o comportamento da classe Soma167, pois a instância é outra.
		
	}
}
