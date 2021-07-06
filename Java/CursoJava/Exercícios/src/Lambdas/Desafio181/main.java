package Lambdas.Desafio181;

import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;

public class main {
    public static void main(String[] args) {

        produto product = new produto("Astra", 27990.00, 8.5);

        BiFunction<Double, Double, Double> realPrice = (price, tax) -> {
           return price * (1 + tax / 100);
        };

        UnaryOperator<Double> municipalTax = RealPrice -> RealPrice >= 2500.00
                    ? RealPrice * (1 + 8.5/100)
                    : RealPrice; 

        UnaryOperator<Double> freigthageTax = PriceWithFreigth -> PriceWithFreigth >= 3000.00
                    ? PriceWithFreigth +  100
                    : PriceWithFreigth;
        
        Function<Double, String> finalResult = Input -> "R$" + Input; 
        
        System.out.println(realPrice.andThen(municipalTax)
                           .andThen(freigthageTax).andThen(finalResult)
                           .apply(product.getPrice(), product.getTax()));

    }
}