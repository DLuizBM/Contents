package Generics;

import java.util.ArrayList;
import java.util.List;

public class Main {

    public static void main(String[] args) {
        Aluno aluno1 = new Aluno("João", "130");
        Aluno aluno2 = new Aluno("Paulo", "131");
        List<Aluno> lst = new ArrayList<>();
        lst.add(aluno1);
        lst.add(aluno2);

        ToUppercase toUppercase = new ToUppercase();
        toUppercase.imprimeNomeMaiusculo2(lst);

    }
}
