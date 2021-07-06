package OO.Heranca.Desafio149;

public class carro {
    
    double velocidade;

    void acelerar(){
        this.velocidade += 5; 
    }

    void frear(){
        if(this.velocidade >= 5) {
            this.velocidade -= 5;
        }
    }
}