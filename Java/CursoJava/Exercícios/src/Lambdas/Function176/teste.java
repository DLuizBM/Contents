package Lambdas.Function176;

import java.util.function.Function;
import java.util.function.Predicate;

public class teste {
    public static void main(String[] args) {
        
        int num = 11;

        Predicate<Integer> testNum = number -> number % 2 == 0;
        Function<Boolean, String> str = isTrue -> isTrue == true ? num + " is par" : num + " is not par";
        Function<String, String> res = result -> result + "!!!";
        System.out.println(str.andThen(res).apply(testNum.test(num)));

    }
}
