package Lambdas.Function176;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

public class main {
    public static void main(String[] args) {
        Function<Integer, String> parOuImpar = numero -> numero % 2 == 0 ? "par" : "impar";

        Integer[] nums = new Integer[2];
        nums[0] = 10;
        nums[1] = 25;
        List<Integer> numbers = Arrays.asList(nums);
        //Generics só aceitam Classes, não tipos primitivos, dessa forma
        //o array se convertido para lista, deve estar declarado como classe, ex Integer
        numbers.forEach(num -> System.out.println(parOuImpar.apply(num)));

        Function<String, String> oResultadoE = result -> {
            return "O resultado é: " + result;
        };

        Function<String, String> empolgado = result -> result + "!!!";

        String resultadoFinal = parOuImpar.andThen(oResultadoE).andThen(empolgado).apply(10);
        // aplique na função parOuImpar o valor 10, a saída dessa aplique como entrada em oResultadoE
        // a saída dessa aplique em empolgado, a saída dessa será o retorno.

        System.out.println(resultadoFinal);
        numbers.forEach(num -> System.out.println(parOuImpar.andThen(oResultadoE).andThen(empolgado).apply(num)));
    }
}