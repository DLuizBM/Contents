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
        String[] str2 = str.get();
        str2[0] = "1";
        str2[1] = "2";
        str2[2] = "3";
        String[] nomes = new String[strings.get().size()];
        nomes = strings.get().toArray(nomes);
        System.out.println(nomes[0]);
        for(String nome: strings.get()){
            System.out.println(nome);
        }
        
    }
}