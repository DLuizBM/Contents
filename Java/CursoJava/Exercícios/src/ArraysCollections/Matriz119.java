package ArraysCollections;

import java.util.Scanner;

public class Matriz119 {
    public static void main(String[] args) {

        Scanner entrada = new Scanner(System.in);
        int alunos = entrada.nextInt();
        int qtdNotas = entrada.nextInt();
        //array externo(linha) e interno(coluna)
        double[][] notas = new double[alunos][qtdNotas];

        for(int i = 0; i < alunos; i++){
            for(int j = 0; j < qtdNotas; j++){
                notas[i][j] = entrada.nextDouble();
            }
        }

        for(int i = 0; i < alunos; i++){
            for(int j = 0; j < qtdNotas; j++){
                System.out.printf(notas[i][j] + " ");
            }
            System.out.println();
        }
        entrada.close();
    }
}