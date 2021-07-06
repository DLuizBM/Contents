package OO.abstract163;

public abstract class Mamifero extends Animal {
    // uma class abstrata pode extender outra classe abstrata

    public abstract String mamar();

    public final String protecao(){
        return "pelos";
    }
    // método final é aquele que não pode ser sobreescrito
    // nas classes filhas
}