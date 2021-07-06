package OO.encapsulamento155.CasaB;

import OO.encapsulamento155.CasaA.ana;

public class julia {
    ana Ana = new ana();
    
    void testeAcesso(){
        //System.err.println(Ana.segredo);
        //System.err.println(Ana.facoDentroDeCasa); // não está dentro do mesmo pacote
        //System.err.println(Ana.formaDefalar); // não recebe nada por herança
        System.err.println(Ana.todosSabem); // a única coisa que se tem acesso é o que está públic

    }
}