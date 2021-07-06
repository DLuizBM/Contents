package ArraysCollections;

import java.util.Arrays;

public class Array116 {
    public static void main(String[] args) {
        // sintaxe para definir arrays
        double[] notas = new double[3];
        notas[0] = 10;
        notas[1] = 9;
        notas[2] = 8;

        System.out.println(notas[0]);
        System.out.println(Arrays.toString(notas));
        // [10, 9, 8]
        for(int i = 0; i < notas.length; i++){
            System.out.println(notas[i]);
        }
        double[] notasAlunos = {1, 2, 3, 4, 5};
    }
}