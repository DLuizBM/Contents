package ArraysCollections;

import java.util.Scanner;

public class Desafio118 {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.println("Quantas notas deseja inserir?");

        int qtd;
        qtd = entrada.nextInt();
        double[] notas = new double[qtd];

        for(int i = 0; i < qtd; i++){
            Scanner entradaNota = new Scanner(System.in);
            double nota = entradaNota.nextDouble();
            notas[i] = nota;
        }

        double tot = 0;

        for(double nota: notas){
            tot += nota;
        }
        System.out.println(tot/notas.length);
    }
}