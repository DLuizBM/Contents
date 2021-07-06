package Lambdas.BinaryBiFunction180;

import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Function;

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