package StreamsAPI.Desafio196;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class Main {
    
    public static void main(String[] args) {
       Predicate<Integer> filterPair = num -> num % 2 == 0;
       Predicate<Integer> filterFive = num -> num % 5 == 0;
       Consumer<Integer> print = System.out::println;
       List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
       nums.stream().filter(filterPair).filter(filterFive).forEach(print);
    }
}
