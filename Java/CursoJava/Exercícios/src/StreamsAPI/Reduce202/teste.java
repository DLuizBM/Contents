package StreamsAPI.Reduce202;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.BinaryOperator;


public class teste {
    public static void main(String[] args) {

        List<String> nums = Arrays.asList("1", "2", "3");
        BiFunction<Double, String, Double> calc = (n1, n2) -> {
            System.out.println("n1 " + n1);
            System.out.println("n2 " + n2);
            return n1 + Integer.parseInt(n2);
        };
        BinaryOperator<Double> comb = (n1, n2) -> {
            System.out.println("CombN1 " + n1);
            System.out.println("CombN2 " + n2);
            return n1 + n2;
        };

        Double d = nums.parallelStream().reduce(1.0, calc, comb);
        // identity: valor inicial
        // accumulator: acumulador
        // reduce com BiFunction<input1, input2, output> x = (n1, n2) -> ...
        // output sempre alimenta o input1 (n1) e o input2 (n2) é alimentado pelo iterável
        // combiner: BinaryOperator que deve receber e retornar o mesmo tipo de identity e de input 1 e input 2
        // nesse caso, o tipo double 
        System.out.println(d);
    }
}

class ParallelStream {

    public static void main(String[] args){
        List<Integer> nums = Arrays.asList(1, 2, 3);
        BinaryOperator<Integer> sum = (ac, n) -> ac + n;

        Integer result = nums.parallelStream().reduce(1, sum);
        System.out.println(result);
        // resultado = 9
        Integer result2 = nums.stream().reduce(1, sum);
        System.out.println(result2);
        // resultado = 7

        /**
         Apesar de result e result2 usarem a mesma lista e ambos iniciarem o reduce
         com 1, o resultado foi diferente por conta do parallelStream.
         Usando parallenStream, as chamadas ao array vão ser paralelas e não sequenciais.
         Ou seja, o array será quebrado em 3 e cada um vai ter sua chamada.
         Dessa forma, para cada chamada o reduce vai usar o valor inicial dado. As chamadas
         serão as seguintes:
         ac + n 
         1  + 1  = 2
         1  + 2  = 3
         1  + 3  = 4
         result  = 9
         Usando somente stream, a chamada será sequencial e as chamadas serão:
         ac + n 
         1  + 1  = 2 -> 2  + 2  = 4 -> 4  + 3  = 7
         result  = 7
         */

    }
}