package ArraysCollections.ExemploEqualsHascode;

import java.util.HashSet;

public class Main {
    
    public static void main(String[] args){
        HashSet<Aluno> conjutoAlunos = new HashSet<Aluno>();

        conjutoAlunos.add(new Aluno(1, "João"));
        conjutoAlunos.add(new Aluno(2, "Sebastião"));

        Aluno alunoBusca = new Aluno(2);

        for(Aluno aluno: conjutoAlunos){
            System.out.println(aluno.hashCode());
        }
        System.out.println("Hashcode aluno de busca: " + alunoBusca.hashCode());
        
        /*
        Se o método hashcode não tiver sido implementado, o hashcode do aluno de busca 
        não vai bater com o hashcode de nenhum aluno dentro do Set conjutoAlunos.
        */

        boolean teste = conjutoAlunos.contains(alunoBusca);
        System.out.println("Existe aluno: " + teste);

        /**
         * Object.equals(null)
         * Apesar do equals na forma primitiva funcionar como o operador ==
         * Ele não compara com null, pois equals é um método e a ivocação desse método
         * com null, gera um NullPointerException.
         */
    }
}
