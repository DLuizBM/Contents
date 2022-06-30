package StreamsAPI.CriandoStream189;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.stream.Stream;

public class main {
    public static void main(String[] args) {
        
        Consumer<String> print = System.out::println;
        int[] nums = new int[] {1, 2, 3};
        //criando uma stream - modo1
        Stream<String> langs = Stream.of("Java", "Python", "C++");
        langs.forEach(print);

        String[] otherLangs = {"Lisp", "Perl", "Go\n"};

        //criando uma stream - modo2
        Stream.of(otherLangs).forEach(print);
        Stream.of(nums).forEach(System.out::println);

        //criando uma stream - modo3
        Arrays.stream(otherLangs).forEach(print);
        Arrays.stream(otherLangs, 1, 2).forEach(print);
        //pega os elementos de índice 1 e vai até 2-1, ou seja, 1

        //criando uma stream - modo4
        List<String> outrasLangs = Arrays.asList("C", "PHP", "HTML\n");
        outrasLangs.stream().forEach(print);
        outrasLangs.parallelStream().forEach(print);

        //criando uma stream - modo5
        //Stream.generate(() -> "a").forEach(print);
        //nesse modo deve-se fazer um supplier( () -> "a" )
        //porém é gerado de forma infinita

        //criando uma stream - modo6
        //Stream.iterate(0, n -> n + 1).forEach(System.out::println);
        //gera de forma infinta, mas ordenada

    }
}