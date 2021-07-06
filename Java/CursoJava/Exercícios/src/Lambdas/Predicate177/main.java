package Lambdas.Predicate177;

import java.util.function.Predicate;

public class main {
    public static void main(String[] args) {
        Predicate<Integer> isPar = num -> num % 2 == 0;
        Predicate<Integer> is3digitos = num -> num >= 100 && num <= 999;
        Predicate<Integer> is220 = num -> {
            return num == 220;
        };
        System.out.println(isPar.test(21));
        //predicate também pode retornar true or false se for usado para comparação
        //composição de lambdas, faz uma comparação booleana entre os dois
        //predicados, se isPar devolve true e is3Digitos também, o resultado é true
        //as duas funções usam o test(220) para testar as condições
        //isPar e executada primeiro
        System.out.println(isPar.and(is3digitos).and(is220).test(220));
    }
}