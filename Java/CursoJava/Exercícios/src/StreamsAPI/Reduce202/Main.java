package StreamsAPI.Reduce202;

public class Main {
    public static void main(String[] args) {
        /**
         * como o retorno do método add é a própria instância, ou seja, 
         * um tipo Mean, é possível fazer esse tipo de operação, instanciar a classe e
         *  já chamar o método
         */
        Mean mean1 = new Mean().add(8.3).add(6.7);
        Mean mean2 = new Mean().add(7.9).add(6.6);
        System.out.println(mean1.getValue());
        System.out.println(Mean.getMeanMatch(mean1, mean2).getValue());
    }
        
}
