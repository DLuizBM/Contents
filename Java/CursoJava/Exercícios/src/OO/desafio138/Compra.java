package OO.desafio138;

import java.util.ArrayList;

public class Compra {

    ArrayList<Item> itens = new ArrayList<Item>();

    void adicionarItem(Item item){
        this.itens.add(item);
    }
    double valorCompra(){
        double total = 0;
        for(Item item: itens){
            total += item.produto.precoProduto * item.quantidade;
        }
        return total;
    }

}