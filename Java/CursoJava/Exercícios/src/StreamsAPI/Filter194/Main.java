package StreamsAPI.Filter194;

import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.List;
import java.util.function.BinaryOperator;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.function.Predicate;

public class Main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Ana", 7.8);
        Aluno a2 = new Aluno("Bia", 8.8);
        Aluno a3 = new Aluno("Gui", 9.8);

        List<Aluno> alunos = Arrays.asList(a1, a2, a3);
        Predicate<Aluno> aprovado = aluno -> aluno.nota >= 8;
        Function<Aluno, String> msg = aluno -> aluno.nome + " está aprovado";
        Consumer<String> print = string -> System.out.println(string);
        // filter pode retornar uma stream menor do que a original
        // retorna o objeto e não só o valor booleano da comparação
        alunos.stream().filter(aprovado).map(msg).forEach(print);

        boolean aproved = aprovado.test(a1);
        System.out.println(aproved);

    }
}
