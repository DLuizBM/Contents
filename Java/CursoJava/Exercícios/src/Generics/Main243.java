package Generics;

import java.util.Arrays;
import java.util.List;

public class Main243 {
    
    public static void main(String[] args) {
        List<Integer> nums = Arrays.asList(1, 2, 3, 4, 5);
        List<Double> numsD = Arrays.asList(1.0, 2.0, 3.0, 4.0, 5.0);

        List<String> strings = Arrays.asList("a", "b", "c", "d");
        Integer numList = (Integer) Generics243.getObject(nums);
        // necessário fazer o cast, pois o método getObject recebe algo genéricos


        Integer numList2 = Generics243.getObject2(nums); // não é necessário o generics, pois ele sabe exatamente o tipo para o qual deve resolver
        Integer numList3 = Generics243.<Integer>getObject2(nums);
        // especificando o tipo Integer que a função deve receber
        // <Integer>getObject2(nums) -> <Integer> especifica que aquilo que getObject2 vai receber
        // deva ser do tipo Integer.
        // nums deve ser um List do tipo Integer
        // Exemplo com Double, especificando <Double> e numsD deve ser um List do tipo Double
        Double numList4 = Generics243.<Double>getObject2(numsD);


        Integer num1 = Generics243.<Integer, Integer, Integer>getObject3(1, 2);
        System.out.println(num1);

    }
}
