package Generics;

public class Aluno extends Pessoa{

    private String matricula;

    public Aluno(){}

    public Aluno(String name, String matricula) {
        super(name);
        this.matricula = matricula;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

}
