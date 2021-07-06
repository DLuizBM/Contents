package OO.GetterSetter158;

public class pessoa {
    
    private int idade;

    // tornando o construtor público
    public pessoa(int Idade){
        setIdade(Idade);
    }

    public int getIdade(){
        return this.idade;
    }

    public void setIdade(int idade){
        this.idade = idade;
    }
}