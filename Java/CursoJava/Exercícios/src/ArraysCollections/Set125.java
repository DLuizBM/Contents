package ArraysCollections;

import java.util.HashSet;
import java.util.Set;
import java.util.SortedSet;
import java.util.TreeSet;

public class Set125 {
    public static void main(String[] args) {
        
        // conjunto homogêneo
        // <>, indica que o set será do tipo especificado, no caso String 
        // isso é chamado de generics
    	
    	// Conjuntos desordenados
        // Set<String> lista = new HashSet<>(); possível das duas formas
    	
    	// Conjuntos ordenados
        SortedSet<String> lista = new TreeSet<>();

        lista.add("Ana");
        lista.add("Carlos");
        lista.add("Luca");
        lista.add("Pedro");

        for(String nome: lista){
            System.out.println(nome);
        }
        
        // Integer, para converter int para a classe Integer
        SortedSet<Integer> nums = new TreeSet<>();

        nums.add(1);
        nums.add(2);
        nums.add(3);
        nums.add(4);
        
        for(int n: nums) {
        	System.out.println(n);
        }
    }
}