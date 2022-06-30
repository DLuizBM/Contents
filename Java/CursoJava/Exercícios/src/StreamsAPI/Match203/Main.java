package StreamsAPI.Match203;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

import StreamsAPI.Filter194.Aluno;

public class Main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Ana", 7.8);
        Aluno a2 = new Aluno("Bia", 8.8);
        Aluno a3 = new Aluno("Gui", 9.8);

        List<Aluno> alunos = Arrays.asList(a1, a2, a3);

        Predicate<Aluno> aprovado = aluno -> aluno.nota >= 7;
        Predicate<Aluno> reprovado = aprovado.negate();

        // allMatch, retorna true se todos os resultados de um teste forem verdadeiros
        // funciona como o all do python
        System.out.println(alunos.stream().allMatch(aprovado));
        // anyMatch, retorna true se pelo menos um resultado de um teste for true
        // funciona como o any do python
        System.out.println(alunos.stream().anyMatch(aprovado));
        // noneMatch, retorna true se nenhum teste for verdadeiro
        System.out.println(alunos.stream().noneMatch(aprovado));
        System.out.println(alunos.stream().noneMatch(reprovado));
        // se nenhum aluno for reprovado, retorna true
        boolean test = alunos.stream().allMatch(aprovado);
        System.out.println(test);
        /**
         * allMatch = true se todos
         * anyMatch = true se algum
         * noneMatch = true se nenhum
         */

    }
}
