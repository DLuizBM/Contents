package OO.desafio138;
import java.util.ArrayList;
public class Cliente {
    String nome;
    ArrayList<Compra> compras = new ArrayList<Compra>();

    void adicionarCompra(Compra compra){
        this.compras.add(compra);
    }
    double valorTotalCompra(){
        double total = 0;
        for(Compra compra: compras){
            total += compra.valorCompra();
        }
        return total;
    }
}