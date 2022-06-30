package StreamsAPI.Other205;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

import StreamsAPI.Filter194.Aluno;

public class Main {

    public static void main(String[] args) {
        Aluno a1 = new Aluno("Ana", 7.1);
        Aluno a2 = new Aluno("Bia", 6.1);
        Aluno a3 = new Aluno("Gui", 8.1);
        Aluno a4 = new Aluno("Gabi", 10.0);
        Aluno a5 = new Aluno("Ana", 7.1);
        Aluno a6 = new Aluno("Bia", 6.1);
        Aluno a7 = new Aluno("Gui", 8.1);
        Aluno a8 = new Aluno("Gabi", 10.0);

        List<Aluno> alunos = Arrays.asList(a1, a2, a3, a4, a5, a6, a7, a8);
        List<Double> notas = alunos.stream().map(a -> a.nota).collect(Collectors.toList());
        Collections.max(notas);
        Collections.min(notas);

        //distinct: serve para eliminar valores repetidos
        //ATENÇÃO: para que o distinct funcione, é necessário implementar o equals hash code na classe aluno
        //nesse exemplo não foi implementado, mas deve ser, caso queira que funcione
        alunos.stream().distinct().forEach(aluno -> System.out.println(aluno.nota));

        //skip/limit, serve para fazer paginação
        //skip: pula uma quantidade de elementos
        //limit: limita quantos elementos eu quero buscar
        System.out.println("SKIP");
        alunos.stream().distinct()
            .skip(3) // pula os 3 primeiro elementos, começa em a4
            .forEach(aluno -> System.out.println(aluno.getName()));

        System.out.println("LIMIT");
        alunos.stream().distinct()
            .limit(3) // busca apenas os 3 primeiros elementos
            .forEach(aluno -> System.out.println(aluno.getName()));
        
        System.out.println("SKIP LIMIT");
        alunos.stream().distinct()
            .skip(3) // pula os 3 primeiros elementos 
            .limit(2) // e depois pega apenas os 2 próximos, ou seja, a4 e a5 
            .forEach(aluno -> System.out.println(aluno.getName()));    
        
        System.out.println("LIMIT SKIP");
        alunos.stream().distinct()
            .limit(2) // busca apenas os 2 primeiros elementos
            .skip(1) // e pula o primeiro, ou seja, pega apenas a2
            .forEach(aluno -> System.out.println(aluno.getName()));
        
        //takeWhile: pegue enquanto determinada condição for satisfeita
        //ex: alunos com nota maior que 7, a função busca enquanto as notas forem maiore que 7
        //se aparecer uma nota menor que 7, ele para, mesmo que após essa haja outras notas maiores
        //que 7

        System.out.println("TAKE WHILE");
        alunos.stream().distinct()
            //.takeWhile(aluno -> aluno.nota > 7)
            .forEach(aluno -> System.out.println(aluno.getName()));
        // a única saída é Ana, elemento a1, pois Ana tem nota maior que 7, logo após Ana, a nota é 6.1
        // como não satisfaz a condição, ele para, mesmo que após  a nota 6.1 haja outras notas maiores que 7


    }
    
}
