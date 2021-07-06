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
