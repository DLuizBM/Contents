package ArraysCollections;

public class test {
    
    public static void main(String[] args) {
        String a = "olá";
        String b = "olá";
        System.out.println(a == b);
        // true
        // pois fazendo a comparação de strings literais
        // o java utliza o mesmo Objeto String para alocar 
        // a variável a e b, logo, eles tem a mesma referência 
        String c = "olá";
        String d = new String("olá");
        System.out.println(c == d);
        // false, pois ao fazer new String, eu crio um novo objeto do tipo String
        // e esse terá outra referência de memória, como == compara a referência,
        // esse será falso.
    }
}
