package OO.Heranca.Desafio149;

public class ferrari extends carro {
    
    // override server apenas para identificar que o método
    // está sobreescrevendo o método de cima
    @Override
    void acelerar(){
        this.velocidade += 15;
    }

    void frear(){
        if(this.velocidade >= 15){
        this.velocidade -= 15;
        }
    }
}