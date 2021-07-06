package OO.polimorfismo159;

public class Jantar {
    public static void main(String[] args) {

        Pessoa p1 = new Pessoa(99);

        Comida arroz = new Arroz(0.2);
        p1.comer(arroz);
        System.out.println(p1.getPeso());

        Comida feijao = new Feijao(0.5);
        p1.comer(feijao);
        System.out.println(p1.getPeso());


    }
}