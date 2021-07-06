package OO.Interface161;

public class ferrari extends carro implements esportivo, luxo {
    
     boolean ligarAr = false;

    ferrari(int velocidade){
        super(velocidade);
    }

    ferrari(){
        super();
    }

    @Override
    public void ligarTurbo() {
        acelerar(15);
    }

    @Override
    public void desligarTurbo() {
        acelerar();
    }

    @Override
    public void ligarAr() {
        this.ligarAr = true;
    }

    @Override
    public void desligarAr(){
        this.ligarAr = false;
    }

}