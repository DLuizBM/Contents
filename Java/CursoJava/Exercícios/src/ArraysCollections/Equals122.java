package ArraysCollections;

public class Equals122 {
    public static void main(String[] args) {

        Usuario122 u1 = new Usuario122();
        u1.nome = "Pedro Silva";
        u1.email = "pedro@gmail.com.br";

        Usuario122 u2 = new Usuario122();
        u2.nome = "Pedro Silva";
        u2.email = "pedro@gmail.com.br";

        System.out.println(u1 == u2);
        // resultado, false, pois está sendo comparado o endereço de memória
        System.out.println(u1.equals(u2));
        // resultado, false, pois o equals dessa forma funciona como o ==
        // ele deve ser trabalhado
        
    }
}