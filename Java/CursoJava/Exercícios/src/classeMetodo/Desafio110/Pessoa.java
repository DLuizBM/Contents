package classeMetodo.Desafio110;

public class Pessoa {
    String nome;
    double peso;

    // passando a variável peso
    double PesoTotal(double pesoComida){
        double novoPeso = this.peso + pesoComida;
        this.peso = novoPeso;
        return novoPeso;
    }

    //passando o objeto comida e extraindo o peso
    double PesoTotal(Comida comida){
        double novoPeso = this.peso + comida.peso;
        this.peso = novoPeso;
        return novoPeso;
    }
}