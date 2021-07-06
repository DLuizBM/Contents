package Generics;

public class Caixa<T> {

    private T coisa;

    public void guardar(T coisa){
        this.coisa = coisa;
    }

    public T abrir(){
        return coisa;
    }

    /**
     * A ideia de generics é definir um tipo genérico em tempo de execução, quando a classe for
     * instanciada, então o tipo é resolvido, substituindo o genérico para o tipo especificado na instância
     * Nessa classe, o atributo coisa, pode receber um tipo Integer, Double, String, ou seja,
     * qualquer tipo.
     */
    
}
