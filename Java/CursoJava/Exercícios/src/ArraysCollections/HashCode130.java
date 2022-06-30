package ArraysCollections;

import java.util.HashSet;

public class HashCode130 {
    public static void main(String[] args) {
        HashSet<Usuario126> usuarios = new  HashSet<Usuario126>();

        usuarios.add(new Usuario126("Pedro"));
        usuarios.add(new Usuario126("Ana"));
        usuarios.add(new Usuario126("Guilherme"));

        boolean resultado = usuarios.contains(new Usuario126("Guilherme"));
        /*
        O hashcode deve ser implementado dentro da classe, para ensinar a classe de la classe
        a fazer a comparação entre os objetos, pois por padrão a classe usa o hashcode da classe 
        Object que é um hashcode para cada instância de objeto. 
        Se não fosse implementado o hashcode para a classe Usuario126, ao fazer
        usuarios.contains(new Usuario126("Guilherme")), a comparação seria false, pois como
        cada objeto teria um hashcode diferente.
        */
        System.out.println(resultado);

    }

    
}