package OO.encapsulamento155.CasaB;

import OO.encapsulamento155.CasaA.ana;

public class pedro extends ana{
    
    //ana Ana = new ana(); não é necessário quando ser herda
    void testeAcesso(){
        //System.err.println(Ana.segredo);
        //System.err.println(Ana.facoDentroDeCasa); não será visível porque não está no mesmo pacote
        System.err.println(formaDefalar);
        // quando algo é transmitido por herança, a acesso não deve ser feito por instância
        // e sim a partir da herança, para isso não é necessário cria uma Ana
        // o acesso é direto
        System.err.println(todosSabem);

    }
}