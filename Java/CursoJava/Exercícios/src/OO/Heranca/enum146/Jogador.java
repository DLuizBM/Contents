package OO.Heranca.enum146;

public class Jogador {
    int x;
    int y;
    int vida = 100;

    Jogador(){
        this(0, 0);
        // this pode ser usado pra chamar outro construtor
        // nesse caso, o this chama o construtor de baixo
        // passando x e y como default
        // esse ainda é o construtor padrão, mas chama um segundo construtor
        // Sem o construtor padrão de forma explícita, não seria possível
        // chamar o super em Heroi
        
    }
    Jogador(int x, int y){
        this.x = x;
        this.y = y;
    }

    boolean atacar(Jogador oponente){
        int deltaX = Math.abs(this.x - oponente.x);
        int deltaY = Math.abs(this.y - oponente.y);

        if(deltaX == 0  && deltaY == 1){
            oponente.vida -= 10;
            return true;
        }else if(deltaX == 0  && deltaY == 0){
            oponente.vida -= 10;
            return true;
        }else{
            return false;
        }
    }

    boolean andar(Direcao direcao){
        if(direcao == Direcao.NORTE){
            y++;
        }
        return true;
    }
}