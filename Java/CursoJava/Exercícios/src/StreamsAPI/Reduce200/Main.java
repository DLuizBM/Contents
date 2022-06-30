package StreamsAPI.Reduce200;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.function.BinaryOperator;

public class Main {
    public static void main(String[] args) {
            List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
            BinaryOperator<Integer> sum = (ac, n) -> {
                System.out.println(ac + " " + n);
                return ac+n;
            };

            // reduce, assim como o forEach, é uma função terminadora, ou seja, após ela 
            // não é possível encadear outra função.
            // reduce quando chamado dessa forma, retorna um Optional, pois pode haver ou não valores.
            //Optional<Integer> total = nums.stream().reduce(sum);
            //System.out.println(total);
            //int totalInt = nums.stream().reduce(sum).get();
            //System.out.println(totalInt);
            // Quando é passado uma valor inicial para o reduce, não é necessário o get, pois há a certeza
            // que algum valor será retornado
            //int totalInt2 = nums.stream().reduce(10, sum);
            //System.out.println(totalInt2);

            Integer totalInt3 = nums.parallelStream().reduce(100, sum);
            System.out.println(totalInt3);
            // não colocando valor inicial, o reduce retorna um optional
            // ifPresente é uma função do optional
            nums.stream().filter(n -> {
                System.out.println("filter");
                if(n > 5){
                    return true;
                }
                return false;
            }).reduce(0, sum);
    }
}

class Reduce {
    
    public static void main(String[] args){
        ///List<Integer> nums = new ArrayList<>();
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5, 6, 7);
        BinaryOperator<Integer> sum = (ac, n) -> ac + n;

        Optional<Integer> result = nums.stream().reduce(sum);
        // Quando não se passa um valor inicial para o reduce, ele inicia o cálculo 
        // usando os dois primeiros elementos do stream.
        System.out.println(result.get());

    }
}
