package OO.abstract163;

public abstract class Animal {

    // Uma classe abstrata é um modelo para outras classes, onde há métodos que podem se adaptar
    // (métodos abstratos) que podem ser implementados de acordo com a necessidade da classe.
    // Ex: 
    /*
    public abstract class conta {

        private int saldo

        public int getSaldo(){
            return this.saldo;
        }

        public void setSaldo(int saldo){
            this.saldo = saldo;
        }

        public abstract int sacar();

    }

    Podemos criar a classe ContaCorrente e a classe ContaPoupanca que herdam da classe abstrata
    Conta, as duras terão o modelo da classe Conta, mas cada uma pode implementar de forma diferente
    o método abstrato sacar
    */
    
    // nessa classe abstrata foi implementado um método (respirar)
    // e outro foi deixado como abstrato(será implementado mais adiante)
    public String respirar(){
        return "Co2";
    }

    public abstract String mover();
    // os métodos ainda não implementados devem ter abstract
}