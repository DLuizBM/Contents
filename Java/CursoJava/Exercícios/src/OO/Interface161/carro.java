package OO.Interface161;

public class carro {
    int velocidade;

    carro(){
        this(100);
    }
    carro(int velocidade){
        this.velocidade = velocidade;
    }

    void acelerar(){
        this.velocidade += 5;
    }

    void acelerar(int acelerar){
        this.velocidade += acelerar;
    }
}