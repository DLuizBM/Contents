package Lambdas.Predicate174;

public class produto {
    
    public String nome;
    public double preco;

    public produto(String nome, double preco){
        this.nome = nome;
        this.preco = preco;
    }

    public String toString(){
        return this.nome + " " + this.preco;
    }
    
    /*
     * System.out.println(produto);
     * Lambdas.Predicate174.produto@5451c3a8: esse é a saída de um objeto produto
     * sem a definição do toString. Quando se usa o toString() é possível customizar 
     * o que ser printado de forma direta, no caso, colocando direto o objeto.
     * System.out.println(produto);
     * notebook 3000.0, saída de um objeto produto, quando se usa o toString()
     */


}