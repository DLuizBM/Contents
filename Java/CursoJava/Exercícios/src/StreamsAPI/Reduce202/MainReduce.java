package StreamsAPI.Reduce202;

import java.util.Arrays;
import java.util.List;
import java.util.function.BiFunction;
import java.util.function.BinaryOperator;
import java.util.function.Function;
import java.util.function.Predicate;

public class MainReduce {

    public static void main(String[] args) {
            
        
        Aluno a1 = new Aluno("Ana", 7.1);
        Aluno a2 = new Aluno("Luna", 6.1);
        Aluno a3 = new Aluno("Gui", 8.1);
        Aluno a4 = new Aluno("Gabi", 10);
        
        List<Aluno> students = Arrays.asList(a1, a2, a3, a4);

        Predicate<Aluno> approved = student -> student.grade >= 7.0;
        Function<Aluno, Double> grades = student -> student.grade;
        BiFunction<Mean, Double, Mean> calcMean = (mean, grade) -> {
            System.out.println("mean " + mean.getValue());
            System.out.println("grade " + grade);
        return mean.add(grade);
        }; 
        BinaryOperator<Mean> matchMean = (m1, m2) -> {
            System.out.println("M1 " + m1.getValue());
            System.out.println("M2 " + m2.getValue());
            return Mean.getMeanMatch(m1, m2);
        };
        Mean mean = students.parallelStream().filter(approved).map(grades).reduce(new Mean(), calcMean, matchMean);
        System.out.println(mean.getValue());

        Mean m11 = new Mean().add(6.9).add(7.0);
        Mean m22 = new Mean().add(7.9).add(8.0);
        System.out.println(Mean.getMeanMatch(m11, m22).getValue());
    }

}
