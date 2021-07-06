package Lambdas.InterfacesFuncionais169;

import java.util.function.BinaryOperator;

public class interfaces170 {

	public static void main(String[] args) {
		// utilizando interfaces do próprio java
		// os generics só suportam classes, por isso Double e não double
		BinaryOperator<Double> calc = (x, y) ->{
			return x + y;
		};
		System.out.println(calc.apply(5.0, 5.0));
		// 5.0, pois o java não permite conversão direta do tipo inteiro literal
		// pro tipo double
	}
}
