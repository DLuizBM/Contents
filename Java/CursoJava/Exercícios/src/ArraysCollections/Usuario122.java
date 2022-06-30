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

public class Main
{
	public static void main(String[] args) {
	    
	    Pessoa p1 = new Pessoa("Messi", "555", "Andrés");
	    Pessoa p2 = new Pessoa("Messi", "555", "Andrés");
	    String a = "Eu";
	    String b = "Eu";
	    
	    String c = new String("Eu");
	    String d = new String("Eu");
	    
		System.out.println(a == b);
        // Retorna true
        // É possível fazer a comparação de Strings com o operador ==
        // A saída é true, pois String a e b estão com os valores definidos na memória
        // o operador == verifica que esses valores são iguais e retorna true
		System.out.println(c == d);
        // Retorna false
        // False pois c e d são instâncias do objeto String, logo, cada instância guarda
        // o valor do endereço de memória de cada uma. Como cada endereço é diferente, o valor é false.
		System.out.println(c.equals(d));
        // Retorna true
        // O método equals compara o valor em cada objeto, como são iguais, retorna true.
		System.out.println(p1.equals(p2));
        // Retorna true
		
		
	}
}

class Pessoa {
    
    String nome;
    String telefone;
    String sobrenome;
    
    Pessoa(String nome, String telefone, String sobrenome){
        this.nome = nome;
        this.telefone = telefone;
        this.sobrenome = sobrenome;
    }
    
    public boolean equals(Object obj){
        
        Pessoa pessoa = (Pessoa) obj;
        
        boolean mesmoNome = this.nome == pessoa.nome;
        boolean mesmoTelefone = this.telefone == pessoa.telefone;
        boolean mesmoSobrenome = this.sobrenome == pessoa.sobrenome;
        return mesmoNome && mesmoTelefone && mesmoSobrenome;
        
    }
    
}