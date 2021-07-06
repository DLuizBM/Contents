package Generics;


public class Main247 {

    public static void main(String[] args) {

        Pares244<Integer, String> result = new Pares244<>();

        result.adicionar(1, "Maria");
        result.adicionar(2, "Gui");
        result.adicionar(3, "Ana");
        result.adicionar(1, "Rebeca");

        System.out.println(result.getValor(1));
        System.out.println(result.getValor(1));
        System.out.println(result.getValor(3));
        
    }
}