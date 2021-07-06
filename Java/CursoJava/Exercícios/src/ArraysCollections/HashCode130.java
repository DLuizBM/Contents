package ArraysCollections;

import java.util.HashSet;

public class HashCode130 {
    public static void main(String[] args) {
        HashSet<Usuario126> usuarios = new  HashSet<Usuario126>();

        usuarios.add(new Usuario126("Pedro"));
        usuarios.add(new Usuario126("Ana"));
        usuarios.add(new Usuario126("Guilherme"));

        boolean resultado = usuarios.contains(new Usuario126("Guilherme"));
        System.out.println(resultado);

    }
}