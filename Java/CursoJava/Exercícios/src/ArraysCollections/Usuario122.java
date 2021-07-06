package ArraysCollections;

public class Usuario122 {

    String nome;
    String email;
    
    // implementando o equals
    public boolean equals(Object objeto) {
        // definindo o critério para comparar 2 objetos
        // é necessário comparar usuário com usuário 
        // para isso deve-se transformar objeto em Usuario

        Usuario122 outro = (Usuario122) objeto;
        boolean nomeIgual = outro.nome == this.nome;
        // nomeIgual recebe true se outro.nome for igual a this.nome
        //boolean emailIgual = outro.email == this.email; pode ser feito de 2 formas
        boolean emailIgual = outro.email.equals(this.email);
        // critério de igualdade
        return nomeIgual && emailIgual;

        // para u1.equals(u2), u1 vai ser o this e u2 outro
    }
    
}