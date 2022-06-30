package Lambdas.UnaryOperator179;

import java.util.function.Function;
import java.util.function.UnaryOperator;

public class main {

    public static void main(String[] args) {
        UnaryOperator<Integer> maisDois = n -> n + 2;
        UnaryOperator<Integer> vezesDois = n -> n * 2;
        UnaryOperator<Integer> aoQuadrado = n -> n * n;
        Function<Integer, Integer> soma = n -> n + 2;
        
        int result = maisDois.andThen(vezesDois).andThen(aoQuadrado).apply(0);
        // apply é o método que inicia o processo.
        // aplique zero na função maisDois, o resultado dessa, aplique em vezesDois
        // o resultado dessa, aplique em aoQuadrado.
        System.out.println(result);

        // Compose: compose faz a operação ao contrário
        int result2 = aoQuadrado.compose(vezesDois).compose(maisDois).apply(0);
        // execute a função maisDois, depois a função vezesDois e por último a função aoQuadrado.
        System.out.println(result2);
        int result3 = soma.andThen(aoQuadrado).apply(10);
        System.out.println(result3);
    }
    

}