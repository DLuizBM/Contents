package Lambdas.Supplier178;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.function.Supplier;

public class main {
    public static void main(String[] args) {
        // supplier fornece algo, pode ser um array, lista, etc
        Supplier<List<String>> strings = () -> Arrays.asList("Divino", "Luiz");
        Supplier<String[]> str = () -> new String[3];
        Supplier<List<Integer>> integerList = () -> new ArrayList<>();
        String[] str2 = str.get();
        str2[0] = "1";
        str2[1] = "2";
        str2[2] = "3";
        String[] nomes = new String[strings.get().size()];
        nomes = strings.get().toArray(nomes);
        // nomes = strings.get().toArray(new String[2]);
        // new String[2] ou nomes dentro do toArray, é necessário para passar o tipo
        // do array, se não fosse passado, seria necessário fazer um cast, como abaixo, 
        // para transformar Object em String[].
        // nomes = (String[]) strings.get().toArray();
        System.out.println(nomes[0]);
        for(String nome: strings.get()){
            System.out.println(nome);
        }
        
    }
}