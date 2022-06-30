package StreamsAPI.Map191;

import java.util.Arrays;
import java.util.List;
import java.util.function.Consumer;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;
import java.util.stream.Collectors;

public class main {
    public static void main(String[] args) {

        Consumer<String> print = System.out::println;

        Stream<String> brands = Stream.of("BMW", "Audi", "Honda");
        List<String> newBrands = Arrays.asList("BMW", "Audi", "Honda");

        brands.map(e -> e.toUpperCase()).forEach(print);
        // brands.filter(e -> e.length() > 3).forEach(print); a stream já foi manipulada na linha anterior, nessa linha será gerado um erro: java.lang.IllegalStateException
        newBrands.stream().map(e -> e.toUpperCase()).forEach(print);

        UnaryOperator<String> maiuscula = n -> n.toUpperCase();
        UnaryOperator<String> firstLetter = n -> n.charAt(0) + "";
        UnaryOperator<String> scream = n -> n + "!!!"; 

        // map gera uma stream de tamanho original, não é possível com o map ter uma stream menor
        newBrands.stream().map(maiuscula)
                          .map(firstLetter)
                          .map(scream)
                          .forEach(print);
        // uma stream só pode ser operada uma vez, se em um conjunto de dados
        // se deseja fazer mais de uma manipulação, ex: linha 19 e 26, deve-se
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

class Main
{
	public static void main(String[] args) {
		List<Integer> nums = Arrays.asList(1, 2, 3);
		List<Integer> newNums = nums.stream().map(num -> num + 10).collect(Collectors.toList());
	}
}

import java.util.List;
import java.util.Arrays;
import java.util.stream.Collectors;
import static java.util.stream.Collectors.toList;

public class MyClass {
    public static void main(String args[]) {
      List<Integer> nums = Arrays.asList(1, 2, 3);
	  List<Integer> newNums = nums.stream().map(num -> num + 10).collect(toList());
    }
}