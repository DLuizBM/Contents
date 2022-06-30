package StreamsAPI.MinMax204;

import java.util.Arrays;
import java.util.Comparator;
import java.util.List;

import StreamsAPI.Filter194.Aluno;

public class Main {
    public static void main(String[] args) {
        Aluno a1 = new Aluno("Ana", 7.1);
        Aluno a2 = new Aluno("Bia", 6.1);
        Aluno a3 = new Aluno("Gui", 8.1);
        Aluno a4 = new Aluno("Gabi", 10.0);

        List<Aluno> alunos = Arrays.asList(a1, a2, a3, a4);

        Comparator<Aluno> maiorNota = (aluno1, aluno2) -> {
            System.out.println("aluno 1 " + aluno1.nota);
            System.out.println("aluno 2 " + aluno2.nota);
            if(aluno1.nota > aluno2.nota) return 1;
            if(aluno1.nota < aluno2.nota) return -1;
            /*
             * O java usa um padrão no comparator
             * x > y, retorna um número positiv (pode ser qualquer positivo), retorna o número à esquerda (o primero objeto é maior que o segundo)
             * x < y, retorna um número negativo (pode ser qualquer negativo), retorna o número à direita  (o segundo objeto é maior que o primeiro)
             * x == y, retorna 0
             */
            return 0;
        };
        
        System.out.println(Integer.compare(3, 1)); // return 1, x > y. A lógica de retorno é default do compare (ver a documentação)

        System.out.println(alunos.stream().max(maiorNota).get().nota);
        System.out.println(alunos.stream().min(maiorNota).get().nota);
        
        // Implementação do compare, max e min, para fixar o entendimento
        System.out.println(Main.max(Main.compare(10, 11), 10, 11));
        System.out.println(Main.min(Main.compare(10, 11), 10, 11));

    }

    static int compare(int a, int b){

        int dif = a - b;

        if(dif > 0){
            return 1;
        }else if(dif < 0){
            return -1;
        }else{
            return 0;
        }

    }

    static int max(int compare, int a, int b){
        if(compare == 1){
            return a;
        }else if(compare == -1){
            return b;
        }else{
            return a;
        }
    }

    static int min(int compare, int a, int b){
        if(compare == 1){
            return b;
        }else if(compare == -1){
            return a;
        }else{
            return a;
        }
    }

}
