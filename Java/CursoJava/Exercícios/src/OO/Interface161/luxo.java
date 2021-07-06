package OO.Interface161;

public interface luxo {
    
    // dentro de interface, todos os métodos são públicos e abstract
    // mas é possível implementar um default, em que se o usuário quiser
    // ele pode implementar ou não o método
    void ligarAr();
    void desligarAr();

    // se necessário, esse método pode ser sobreescrito
    // se não, apresentará sempre esse comportamento
    default int velocidadeAr(){
        return 1;
    }

    default int velocidadeCruzeiro(){
        return 80;
    }
}