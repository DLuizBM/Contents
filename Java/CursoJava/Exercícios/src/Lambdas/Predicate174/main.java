package Lambdas.Predicate174;

import java.util.function.Predicate;

public class main {
    public static void main(String[] args) {

        // predicate funciona como um filtro
        // retorna boolean
        Predicate<produto> isCaro = produto -> produto.preco > 20000.00;

        produto carro = new produto("carro", 25000.00);

        System.out.println(isCaro.test(carro));
    }
}