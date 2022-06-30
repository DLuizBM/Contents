package Pilha;

public class No {

    private int dado;
    private No noRef = null;

    public No(){

    }

    public No(int dado) {
        this.dado = dado;
    }

    public int getDado() {
        return dado;
    }

    public void setDado(int dado) {
        this.dado = dado;
    }

    public No getNoRef() {
        return noRef;
    }

    public void setNoRef(No noRef) {
        this.noRef = noRef;
    }

    @Override
    public String toString() {
        return "No{" +
                "dado=" + dado +
                '}';
    }
}
