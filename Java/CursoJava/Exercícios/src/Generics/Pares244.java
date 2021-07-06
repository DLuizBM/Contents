package Generics;

import java.util.HashSet;
import java.util.Optional;
import java.util.Set;

public class Pares244<C extends Number, V> {
    // o tipo C deve ser do tipo Number
    
    private final Set<ChaveValor<C, V>> itens = new HashSet<>();
    // SortedSet do tipo criado ChaveValor

    public void adicionar(C chave, V valor){
        if(chave == null) return; //essa condição faz o programa simplesmente sair do método e nada é executado.
        
        ChaveValor<C, V> novoPar = new ChaveValor<C,V>(chave, valor);
        
        if(itens.contains(novoPar)){ // graças ao equals e hash code ele vai fazer a verificação pela chave
            itens.remove(novoPar);
        }

        itens.add(new ChaveValor<C, V>(chave, valor));
    }

    public V getValor(C chave){
        if(chave == null) return null;

        Optional<ChaveValor<C, V>> parOptional = itens
        .stream().filter(p -> p.getChave().equals(chave)).findFirst();

        return parOptional.isPresent() ? parOptional.get().getValor() : null;
    }
}
