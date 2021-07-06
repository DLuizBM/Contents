package ArraysCollections;

import java.util.HashSet;

public class Set124 {
    @SuppressWarnings({"rawtypes", "unchecked"}) // retira as advertências do conjunto
    public static void main(String[] args) {
        // forma não correta de criar o conjunto
        HashSet conjunto = new HashSet();

        // add -> método para adicionar no conjunto
        conjunto.add(1.2); // automaticamente 1.2 é convertido de double para a classe Double
        conjunto.add(true); // boolean para Boolean
        conjunto.add("Teste"); // String já é objeto
        conjunto.add(1); // int para Integer

        // tamanho do conjunto
        System.out.println(conjunto.size());
        // removendo do conjunto, retorna true or false
        System.out.println(conjunto.remove(1.2));
        // contains -> verifica se um elemento está no conjunto
        System.out.println(conjunto.contains(1));

        HashSet nums = new HashSet();
        nums.add(1);
        nums.add(2);
        nums.add(3);

        //União de conjuntos
        //conjunto.addAll(nums);
        System.out.println(conjunto);

        // Intersecção de conjuntos
        conjunto.retainAll(nums);
        System.out.println(conjunto);

        // Limpa o conjunto
        conjunto.clear();

    }
}