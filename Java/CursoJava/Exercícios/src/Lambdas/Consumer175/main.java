package Lambdas.Consumer175;

import java.util.ArrayList;
import java.util.function.Consumer;

import Lambdas.Predicate174.produto;

public class main {
    public static void main(String[] args) {
        // consumer recebe apenas um parâmetro e não retorna nada

        Consumer<produto> prod = p -> System.out.println(p.nome);
        // se escreve a expressão que vai ser usada, ou seja, cada objeto
        // produto vai ser "analisado" dessa forma

        produto p1 = new produto("notebook", 3000.00);
        produto p2 = new produto("celular", 2000.00);
        produto p3 = new produto("tablet", 1000.00);

        ArrayList <produto> produtos = new ArrayList<>();
        produtos.add(p1);
        produtos.add(p2);
        produtos.add(p3);

        produtos.forEach(prod);
        produtos.forEach(System.out::println);
        System.out.println(p1 + "!!!!");
        prod.accept(produtos.get(0));
        // para cada produto em produtos, aplique o prod
        // a sobreescrita do método toString, faz printar o nome e o preço de cada produto
        /*
        * System.out.println(produto);
        * Lambdas.Predicate174.produto@5451c3a8: esse é a saída de um objeto produto
        * sem a definição do toString. Quando se usa o toString() é possível customizar 
        * o que ser printado de forma direta, no caso, colocando direto o objeto.
        * System.out.println(produto);
        * notebook 3000.0, saída de um objeto produto, quando se usa o toString()
        */
    }
}