package Lambdas.BinaryBiFunction180;

import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;

public class main {
    public static void main(String[] args) {
        // Esse operador retorna o mesmo tipo, se entra com double, retorna double
        BinaryOperator<Double> media = (n1, n2) -> (n1 + n2) / 2;

        System.out.println(media.apply(7.9, 8.2));

        BiFunction<Double, Double, String> result = (n1, n2) -> {
            return ((n1 + n2)/2 >= 7 ? "aprovado" : "reprovado");
        }; 

        System.out.println(result.apply(7.0, 6.0));

        Function<Double, String> conceito = m -> m >= 7 ? "Aprovado" : "Reprovado";
        // a entrada é um double e a saída uma string

        System.out.println(media.andThen(conceito).apply(6.7, 5.1));
    }
}

class Main
{
	public static void main(String[] args) {
	    
	    Function<Integer, Integer> calculo = x -> x + 10;
	    BinaryOperator<Integer> calculo2 = (x, y) -> x * y;
	    Function<Integer, Integer> calculo3 = x -> x + 25;
	    Predicate<Integer> isCaro = x -> x > 25;

	    Integer num = 10;
	    
	    System.out.println(isCaro.test(calculo2.andThen(calculo).andThen(calculo3).apply(5, 5)));

		
	}
}