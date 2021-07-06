package classeMetodo.Desafio110;

public class Jantar {
    public static void main(String[] args) {
        // criando a pessoa
        Pessoa p1 = new Pessoa();
        p1.nome = "Divino";
        p1.peso = 89;

        // criando as comidas
        Comida c1 = new Comida("feijão", 0.230);
        Comida c2 = new Comida("Arroz", 0.300);
        Comida c3 = new Comida("Frango", 0.5);

        p1.PesoTotal(c1.peso);
        System.out.println(p1.peso);

        p1.PesoTotal(c2.peso);
        System.out.println(p1.peso);

        p1.PesoTotal(c3);
        System.out.println(p1.peso);


    }
}