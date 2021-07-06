package OO;

import java.util.ArrayList;

public class Compra136 {

	String cliente;
	ArrayList<Item136> itens = new ArrayList<Item136>();
	
	double getValorTotal() {
		double tot = 0;
		for(Item136 item: itens) {
			tot += item.quantidade * item.preco;
		}
		return tot;
	}
	
}
