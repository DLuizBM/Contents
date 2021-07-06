package OO;

public class CompraTeste136 {

	public static void main(String[] args) {
		
		Compra136 c1 = new Compra136();
		c1.cliente = "João";
		
		c1.itens.add(new Item136("caneta", 20, 7.45));
		c1.itens.add(new Item136("Borracha", 12, 3.89));
		// como o relacionamento é um para muitos
		// um cliente pode comprar vários itens
		System.out.println(c1.itens.size());
		System.out.println(c1.getValorTotal());
	}
}
