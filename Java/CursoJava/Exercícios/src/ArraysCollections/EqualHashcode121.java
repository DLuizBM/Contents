package ArraysCollections;

public class EqualHashcode121 {
    /**
     * Se forem declarados dois objetos como os mesmos atributos
     * e os atributos estiverem com o mesmo valor
     * se for feita uma comparação do obj1 == obj2
     * o resultado será falso, isso porque na comparação
     * de objetos será comparado o endereço de memória
     * como cada um aponta para um endereço de memória diferente
     * o resultado será falso
     * 
     * Equals é um método que por padrão está em todos os objetos em JAVA
     * mesmo nos criados pelo desenvolvedor
     * Equals é a função em JAVA que compara dois objetos, retorna true or false
     * Hashcode é um método de separação de elementos, separa os que tem hashcode
     * iguais, para só aí ser aplicado o equals, ex: em uma lista de nomes em que 
     * se deseja saber quais nomes são iguais, ao aplicar o hashcode, serão separados
     * os nomes que, por exemplo, tenho a mesma quantidade de letras, diminuindo muito
     * a quantidade de comparações para saber quantos nomes são iguais
     */
}