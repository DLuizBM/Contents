package StreamsAPI.Map191;

import java.util.function.UnaryOperator;

public class Utilitarios {
    
    public final static UnaryOperator<String> maiuscula = n -> n.toUpperCase();


    public final static UnaryOperator<String> firstLetter = n -> n.charAt(0) + "";


    public final static String scream(String n) {
        return n + "!!!";
    }


}