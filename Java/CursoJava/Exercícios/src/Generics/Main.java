package Generics;

public class Main {
    public static void main(String[] args) {
        
        Caixa<String> caixaA = new Caixa<>();
        caixaA.guardar("Coisas");
        System.out.println(caixaA.abrir());

        Caixa<Integer> caixaB = new Caixa<>();
        caixaB.guardar(12345);
        System.out.println(caixaB.abrir());

        Caixa caixaC = new Caixa<>();
        caixaC.guardar(10.1); 
        Double num = (Double) caixaC.abrir();
        System.out.println(num);

        /*
         * Os objetos caixaA e caixaB, utilizam o conceito de generics, notar que os dois apesar
         * de serem objetos Caixa, são caixas diferentes, um é double e o outro integer. O generics
         * define que o um objeto pode assumir qualquer tipo, mas quando o tipo é definido, ele fica amarrado
         * naquele tipo. Isso traz vantagens, como por exemplo trabalhar somente com os tipos definidos, 
         * evitando assim ter que fazer casts para garantir que o tipo está correto, como por exemplo, em 
         * caixaC, onde foi usado o tipo mais genérico possível, o Object. Observar a linha 16, em que foi preciso
         * fazer um cast para que a variável num (Double), pudesse receber o valor vindo de caixaC.abrir().
         * Usando object, é possível que uma conversão seja errada, é ao executar o programa, ele lance uma exceção.
         * Usando generics, o JAVA garante os tipos, exigindo que o programador coloque o tipo certo para cada atributo e
         * quando isso não é feito, o programa nem chega a compilar.
         *  
         */
    }
}
