package ArraysCollections.ExemploEqualsHascode;

public class Aluno {

    private String name;
    private int code;

    public Aluno(int code, String name) {
        this.code = code;
        this.name = name;
    }

    public Aluno(int code){
        this.code = code;
    }
    
    @Override
    public int hashCode() {
        return code * 2;
    }

    // Cada instância vai ter seu hashcode formado a partir do code passa na criação
    // da instância. Se forem criadas 10 instâncias com code igual a 10, então todos
    // as 10 instâncias terão o mesmo hashcode.

    @Override
    public boolean equals(Object obj){
        Aluno other = (Aluno) obj;
        boolean equal = this.code == other.code;
        return equal;
    }
    
}
