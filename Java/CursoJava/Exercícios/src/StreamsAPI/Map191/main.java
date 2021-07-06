package StreamsAPI.Map191;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;

public class main {
    public static void main(String[] args) {

        Consumer<String> print = System.out::println;

        Stream<String> brands = Stream.of("BMW", "Audi", "Honda");
        List<String> newBrands = Arrays.asList("BMW", "Audi", "Honda");

        brands.map(e -> e.toUpperCase()).forEach(print);
        newBrands.stream().map(e -> e.toUpperCase()).forEach(print);

        UnaryOperator<String> maiuscula = n -> n.toUpperCase();
        UnaryOperator<String> firstLetter = n -> n.charAt(0) + "";
        UnaryOperator<String> scream = n -> n + "!!!"; 

        // map gera uma stream de tamanho original, não é possível com o map te uma stream menor
        newBrands.stream().map(maiuscula)
                          .map(firstLetter)
                          .map(scream)
                          .forEach(print);
        // uma stream só pode ser operada uma vez, se em um conjunto de dados
        // se deseja fazer mais de uma manipulação, ex: linha 18 e 23, deve-se
        // usar o método de declaração de stream com array, o método da linha 14
        // só permite manipular a stream uma vez, se for tentado manipular outra vez
        // será gerado erro

        System.out.println("/n/n");
        newBrands.stream().map(Utilitarios.maiuscula)
                          .map(firstLetter)
                          .map(Utilitarios::scream) // esse o method reference
                          .forEach(print);
        // method reference: passa a classe :: e a função que se deve executar
        // a função scream em Utilitários recebe uma string e devolve uma string  
    }
}