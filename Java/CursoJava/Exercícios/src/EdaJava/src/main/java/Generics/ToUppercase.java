package Generics;

import java.util.List;
import java.util.Locale;

public class ToUppercase {

    public ToUppercase(){

    }

    public void imprimeNomeMaiusculo1(List<?> alunosNomes){
        //Unknown wildcard: recebe uma lista de qualquer tipo
        for(Object aluno: alunosNomes)
            System.out.println(aluno);
    }

    public void imprimeNomeMaiusculo2(List<? extends Pessoa> alunos){
        //UpperBounded wildcard: só recebe lista de Pessoa ou de objetos que herdem de pessoas
        //na classe main, foi passado uma lista de alunos, que extende Pessoa
        for(Pessoa aluno: alunos)
            System.out.println(aluno.getName().toUpperCase());
    }

    public void imprimeNomeMaiusculo3(List<? super Pessoa> alunos){
        // LowerBounded wildcard: só recebe lista de objetos que Pessoa extend, ou seja, tudo que é pai de Pessoa
        // Se herdeiro de pessoa, exemplo, Aluno, não recebe
        // Ex: classes, Avo, Pai, Filho. Filho extends Pai, Pai extends Avo;
        // List<? extends Pai>, só recebe listas de Avo.
        for(Object aluno: alunos)
            System.out.println(aluno);
    }

}
