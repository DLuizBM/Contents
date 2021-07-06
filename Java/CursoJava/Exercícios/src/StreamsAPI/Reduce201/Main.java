package StreamsAPI.Reduce201;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.stream.Stream;

public class Main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Ana", 7.1);
        Aluno a2 = new Aluno("Luna", 6.1);
        Aluno a3 = new Aluno("Gui", 8.1);
        Aluno a4 = new Aluno("Gabi", 10);
        
        List<Aluno> students = Arrays.asList(a1, a2, a3, a4);

        Predicate<Aluno> approved = student -> student.grade >= 7.0;
        Function<Aluno, Double> grade = student -> student.grade;
        BinaryOperator<Double> sum = (ac, n) -> {
            return ac + n;
        };

        Stream<Double> str = students.stream().filter(approved).map(grade);
        System.out.println(str);
        //passando os dados para outra stream, para que se possa trabalhar em outros lugares
        students.stream().filter(approved).map(grade).reduce(sum).ifPresent(System.out::println);
        Integer[] numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
        BinaryOperator<Integer> a = (ac, n) -> {
            System.out.println("Acumulador" + ac);
            System.out.println(n);
            return ac + n;
        };
        Arrays.asList(numbers).stream().reduce(a).ifPresent(System.out::println);
    }
}
