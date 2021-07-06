package StreamsAPI.Desafio192;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;

public class main implements functions {
    public static void main(String[] args) {

        List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9);
        Consumer<Integer> print = System.out::println;

        numbers.stream().map(functions.intToBinary)
                        .map(str -> new main().reverseString(str))
                        .map(functions.convertStringInInt)
                        .forEach(print);
        
    }
    @Override
    public String reverseString(String str) {
        return new StringBuilder(str).reverse().toString();
    }
}