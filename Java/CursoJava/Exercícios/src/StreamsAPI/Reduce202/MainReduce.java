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
        System.out.println("MEAN");
        Mean mean = students.parallelStream().filter(approved).map(grades).reduce(new Mean(), calcMean, matchMean);
        /*
         Usando parallelStream, serão criadas 3 instâncias da classe Mean, pois serão 3 notas que passarão pelo filtro.
         O programa executa primeiro a função lambda calcMean adicionando m cada uma dessas instâncias a nota do aluno.
         Ao termino da execução da lambda calcMean, existirão as seguintes instâncias de Mean:
         
         m1.total = 7.1;
         m1.numbers = 1;
         
         m2.total = 8.1;
         m2.numbers = 1;

         m3.total = 10;
         m3.numbers = 1;
         
         Após a calcMean, será executada a lambda matchMean. Ela vai juntar as 3 instâncias em uma só, graças a função
         getMeanMatch e tem-se:

         M1.total = m1.total + m2.total
         M1.numbers = m1.numbers + m2.numbers

         M2.total = M1.total + m3.total
         M2.numbers = M1.numbers + m3.numbers

         M2.total = 25.2
         M2.numbers = 3

         media = 25.2/3 = 8.4
         */
        System.out.println("MEAN2");
        Mean mean2 = students.stream().filter(approved).map(grades).reduce(new Mean(), calcMean, matchMean);

        /*
        Usando stream, será adicionado uma instância de Mean (passado em reduce(new Mean(), ...) e todas as notas serão adicionadas a ela. Já que funciona de forma sequencial
        Dentro de calcMean:

        Na primeira chamada, é passada uma instância de Mean, que vamos chamar de m1.

        m1.total = 7.1
        m1.numbers = 1
        
        Como é sequencial, ao chamar o calcMean novamente para a segunda nota, a instância passada continua sendo m1.

        m1.total = 7.1 + 8.1 = 15.2
        m1.numbers = 1 + 1 = 2

        Como é sequencial, ao chamar o calcMean novamente para a terceira nota, a instância passada continua sendo m1.

        m1.total = 15.2 + 10 = 25.2
        m1.numbers = 2 + 1 = 3

        Como só há uma instância de Mean, não é necessário chamar matchMean para agrupar as instâncias, por isso, o programa nem
        entra nessa lambda e não printa o que está dentro.        

        */
        // filter retorna o objeto que possui nota maior ou igual a 7.
        System.out.println(mean.getValue());
        System.out.println(mean2.getValue());

        Mean m11 = new Mean().add(6.9).add(7.0);
        Mean m22 = new Mean().add(7.9).add(8.0);
        System.out.println(Mean.getMeanMatch(m11, m22).getValue());
    }

}

class test {

    public static void main(String[] args){

        Aluno a1 = new Aluno("Ana", 7.1);
        Aluno a2 = new Aluno("Luna", 6.1);
        Aluno a3 = new Aluno("Gui", 8.1);
        Aluno a4 = new Aluno("Gabi", 10);
        
        List<Aluno> students = Arrays.asList(a1, a2, a3, a4);

        Predicate<Aluno> approved = student -> student.grade >= 7.0;
        students.parallelStream().filter(approved).forEach(aluno -> System.out.println(aluno.grade));

    }
}