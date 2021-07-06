package OO.polimorfismo159;

public class Comida {
    
    protected double peso;

    public Comida(){
        this(0);
    }

    public Comida(double peso) {
        this.peso = peso;
    }

    public double getPeso(){
        return peso;
    }

    public void setPeso(double peso){
        if(peso >= 0) {
            this.peso = peso;
        }
    }
}