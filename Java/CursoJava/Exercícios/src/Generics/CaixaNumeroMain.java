package Generics;

public class CaixaNumeroMain {

    public static void main(String[] args) {
        CaixaNumero<Double> number = new CaixaNumero<>();
        number.guardar(25.6);
        System.out.println(number.abrir());
    }
    
    
}
