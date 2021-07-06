package OO.desafio138;

public class Main {
    public static void main(String[] args) {
        // criando produto
        String nomeP1 = "coca";
        double precoP1 = 5;
        Produto p1 = new Produto(nomeP1, precoP1);

        // criando produto2
        String nomeP2 = "pizza";
        double precoP2 = 12;
        Produto p2 = new Produto(nomeP2, precoP2);

        // criando o item
        int qtdP1 = 3;
        Item item1 = new Item(p1, qtdP1);

        // criando o item2
        int qtdP2 = 1;
        Item item2 = new Item(p2, qtdP2);

        // Criando a compra
        Compra compraP1 = new Compra();
        compraP1.adicionarItem(item1);

        // Criando a compra2
        Compra compraP2 = new Compra();
        compraP2.adicionarItem(item2);
        compraP2.adicionarItem(item1);
        
        // Criando o cliente
        Cliente c1 = new Cliente();
        c1.nome = "Divino";
        c1.adicionarCompra(compraP1);

        System.out.println(c1.valorTotalCompra());

        c1.adicionarCompra(compraP2);

        System.out.println(c1.valorTotalCompra());


    }
}