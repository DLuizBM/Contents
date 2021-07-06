package StreamsAPI.ListIteratorStream187;

import java.util.Arrays;
import java.util.Iterator;
import java.util.List;
import java.util.stream.Stream;

public class main {
    public static void main(String[] args) {

        List<String> aprovados = Arrays.asList("Lu", "Gui", "Ana", "Luca");

        System.out.println("Com forEach");
        /*
        for(String aprovado: aprovados){
            System.out.println(aprovado);
        }*/
        aprovados.forEach(item -> System.out.println(item));

        System.out.println("Com iterator");
        Iterator<String> it = aprovados.iterator();
        while(it.hasNext()){
            System.out.println(it.next());
        }

        System.out.println("Com Stream");
        Stream<String> stream = aprovados.stream();
        stream.forEach(System.out::println);
        // no stream o laço acontece de forma interna
        /*
        Um stream tem 3 grupos de operações
        1 - Built ops: operações de construção, que são para chamar e 
        construir os streams;
        2 - Internal ops: operações que recebem uma stream e devolve outra
        stream, possui métodos que ajudam a manipular o stream;
        3 - Terminal ops: operações que recebem uma strema e devolvem outro
        tipo de variável, ex: entra stream e sai um double

        Streams podem ser ordenadas ou não e sequenciais ou paralelas
        */
    }
}