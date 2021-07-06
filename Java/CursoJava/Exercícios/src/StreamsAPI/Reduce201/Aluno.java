package StreamsAPI.Reduce201;

public class Aluno {
    
    String name;
    double grade;
    private boolean goodBehavior;

    public Aluno(String name, double grade){
        this(name, grade, true);
    }

    public Aluno(String name, double grade, boolean goodBehavior){
        this.name = name;
        this.grade = grade;
        this.goodBehavior = goodBehavior;
    }

}
