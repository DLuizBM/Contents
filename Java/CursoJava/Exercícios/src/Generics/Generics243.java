package Generics;

import java.util.List;

public class Generics243 {
    
    // ?: lista de qualquer coisa, ou seja, object
    public static Object getObject(List<?> list){
        return list.get(list.size() -1);
    }

    // <T>:a função tem um tipo T, nesse caso a List<T>, o tipo está associado ao que a função vai receber
    // A função retorna o tipo T.
    // Essa abordagem evita o uso de casts, pois o tipo recebido será exatamente o tipo retornado
    // Essa forma de criar a função é usada quando ela é static
    public static <T> T getObject2(List<T> list){
        return list.get(list.size() -1);
    }

    public static <T, U, V> V getObject3(T paramT, U paramU){ 
        V variable = (V) paramT;
        return variable;
    }

}
