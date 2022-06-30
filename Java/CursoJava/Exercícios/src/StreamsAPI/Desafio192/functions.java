package StreamsAPI.Desafio192;

import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.UnaryOperator;

public interface functions {
    
    Function<Integer, String> intToBinary = num -> Integer.toBinaryString(num);
    public String reverseString(String str);
    Function<String, Integer> convertStringInInt = str -> Integer.parseInt(str, 2);
    UnaryOperator<Double> square = num -> num * num;
}