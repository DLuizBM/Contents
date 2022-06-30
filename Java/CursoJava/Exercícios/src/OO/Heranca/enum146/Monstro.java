package OO.Heranca.enum146;

public class Monstro extends Jogador {
    
    Monstro(){
        this(0, 0);
    }
     Monstro(int x, int y){
        super(x, y);
     }

     // this chama o segundo construtor
     // o segundo contrutor aponta para a classe pai
}