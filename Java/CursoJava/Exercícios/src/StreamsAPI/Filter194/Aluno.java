package StreamsAPI.Filter194;

public class Aluno {
    
    String nome;
    public double nota;

    public Aluno(String nome, double nota){
        this.nome = nome;
        this.nota = nota;
    }

    public String getName(){
        return nome;
    }

    @Override
    public int hashCode() {
        int letters = this.nome.length();
        int nota = (int) this.nota;
        return letters + nota;
    }

    @Override
    public boolean equals(Object obj) {
        Aluno other = (Aluno) obj;
        boolean name = this.nome.equals(other.nome);
        boolean nota = this.nota == other.nota;
        // equals não é aplicado para variáveis primitivas, somente para comparar objetos
        // pois equals é um método.
        return name && nota;
    }
}
