package OO.Heranca.Desafio149;

public class main {
    public static void main(String[] args) {
        
        civic c = new civic();
        c.velocidade = 100;
        c.ligarModoEco();
        c.acelerar();
        // civic herdou o método acelerar de carro
        System.out.println(c.velocidade);

        ferrari f = new ferrari();
        f.velocidade = 100;
        f.acelerar();
        System.out.println(f.velocidade);

        carro carro = new ferrari();
        carro = new civic();
        // Poliformis dinâmico
    }
}