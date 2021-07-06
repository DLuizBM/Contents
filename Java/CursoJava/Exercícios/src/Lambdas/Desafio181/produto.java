package Lambdas.Desafio181;

public class produto {

    private String name;
    private Double price;
    private Double tax;

    public produto(String name, Double price, Double tax){
        this.name = name;
        this.price = price;
        this.tax = tax;
    }

    public Double getPrice(){
        return price;
    }

    public Double getTax(){
        return tax;
    }

}