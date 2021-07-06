package ArraysCollections;

import java.util.ArrayList;

public class List126 {

	public static void main(String[] args) {
		
		// está sendo criado uma lista do tipo Usuario126, que é a classe criada
		// dessa forma, a lista conterá vários objetos desse tipo
		ArrayList<Usuario126> lista = new ArrayList<Usuario126>();
		
		Usuario126 u1 = new Usuario126("Ana");
		lista.add(u1);
		lista.add(new Usuario126("Carlos"));
		lista.add(new Usuario126("Lia"));
		lista.add(new Usuario126("Bia"));
		// get -> pega o valor do índice dado
		System.out.println(lista.get(3).nome);
		for(Usuario126 u: lista) {
			System.out.println(u.nome);
		}
		System.out.println(lista.remove(1).nome);
	}
}
