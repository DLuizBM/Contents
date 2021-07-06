package ArraysCollections;

import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;

public class Map130 {

	public static void main(String[] args) {
		// map possui uma estrutura chave/valor
		Map<Integer, String> usuario = new HashMap<Integer, String>();
		// o método put, adiciona e se houver valor para uma chave
		//ele substitui
		// não pode haver duplicação na chave
		// as chaves formam um conjunto - até por isso não pode haver repetição
		usuario.put(1, "Roberto");
		usuario.put(1, "Ricardo");
		usuario.put(2, "Rafaela");
		usuario.put(3, "Rebeca");

		
		System.out.println(usuario.size());
		System.out.println(usuario.isEmpty());
		System.out.println(usuario.keySet());
		System.out.println(usuario.values());
		System.out.println(usuario.entrySet()); // pega a chave valor ao mesmo tempo
		System.out.println(usuario.containsKey(3)); // verifica se existe a chave
		System.out.println(usuario.containsValue("Rebeca")); // verifica se existe tal valor
		// contaiskey e conteisValue retornam booleano
		System.out.println(usuario.get(4));
		// retorna o valor que está presente naquela chave
		System.out.println(usuario.remove(1));
		// se for adicionado um novo valor para uma chave já existente
		// o valor daquela chave é substituío
		usuario.put(3, "Alberto");
		System.out.println(usuario.get(3));
		
		for(int chave: usuario.keySet()) {
			System.out.println(chave);
		}
		
		for(String valor: usuario.values()) {
			System.out.println(valor);
		}
		for(Entry<Integer, String> registro: usuario.entrySet()) {
			System.out.println(registro.getKey());
			System.out.println(registro.getValue() );
		}
	}
}
