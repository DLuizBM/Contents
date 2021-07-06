package OO.abstract163;

public abstract class Animal {
    
    // nessa classe abstrata foi implementado um método (respirar)
    // e outro foi deixado como abstrato(será implementado mais adiante)
    public String respirar(){
        return "Co2";
    }

    public abstract String mover();
    // os métodos ainda não implementados devem ter abstract
}