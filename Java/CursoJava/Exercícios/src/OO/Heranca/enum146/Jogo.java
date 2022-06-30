package OO.Heranca.enum146;

public class Jogo {
    public static void main(String[] args) {
        Jogador j1 = new Jogador();
        j1.x = 10;
        j1.y = 10;

        Jogador j2 = new Jogador();
        j2.x = 10;
        j2.y = 11;

        j1.atacar(j2);

        System.out.println(j1.vida);
        System.out.println(j2.vida);

        Heroi heroi = new Heroi();
        Direcao dir = Direcao.NORTE;
        heroi.x = 10;
        heroi.y = 11;
        System.out.println("Posição 1: " + heroi.y);
        heroi.andar(dir);
        System.out.println("Posição 2: " + heroi.y);
        heroi.atacar(j1);
        // heroi é um jogador, logo tem os mesmo atributos e métodos
        // como o método atacar está definido para um tipo genérico
        // jogador, herói pode utilizálo
        System.out.println(j1.vida);

        Monstro monstro = new Monstro();
        System.out.println("Posição x do monstro " +monstro.x);
    }
}