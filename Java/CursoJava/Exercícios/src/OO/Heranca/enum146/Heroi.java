package OO.Heranca.enum146;
// extends significa que a classe vai herdar de outra
// no caso, heroi herda de jogador
// heroi também vai ser um jogador, logo ele herda tudo de jogador
public class Heroi extends Jogador{

    // super chama por padrão o construtor padrão da classe pai
    // o construtor padrão é o super
    Heroi(){
        super();
    }
    // se não houvesse o construtor padrão de forma explícita em Jogador
    // deveria ser passado os valores de x e y
    //Heroi(){
        //super(0, 0);
    //}

    
    // sobreescrevendo o método atacar da classe pai
    // herói tem um ataque mais forte que o normal descrito em jogador
    /*
    boolean atacar(Jogador oponente){
        int deltaX = Math.abs(this.x - oponente.x);
        int deltaY = Math.abs(this.y - oponente.y);

        if(deltaX == 0  && deltaY == 1){
            oponente.vida -= 20;
            return true;
        }else if(deltaX == 0  && deltaY == 0){
            oponente.vida -= 20;
            return true;
        }else{
            return false;
        }
    }
    */
    // se quiséssemos usar o método da classe pai
    boolean atacar(Jogador oponente){
        boolean ataque1 = super.atacar(oponente);
        boolean ataque2 = super.atacar(oponente);
        // super chama o método da classe pai
        return ataque1 || ataque2; 
    }
}