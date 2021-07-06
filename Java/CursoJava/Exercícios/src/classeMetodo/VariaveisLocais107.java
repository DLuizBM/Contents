package classeMetodo;

public class VariaveisLocais107 {
    /**
     * Variáveis locais são variáveis definidas dentro de métodos
     * elas ficam visíveis apenas no escopo do método
     * Variáveis de instância são acessíveis a todos os métodos na classe
     * 
     */

    String mes = "Agosto"; 
    // variável de instância/classe, dentro da classe VariaveisLocais107
    // mas fora de métodos
    String data(){
        String dia = "01"; // variável local
        return dia;
    }

    // Valores padrão de variáveis de instância
    // são inicializadas por padrão
    /**
     * byte, short, int, long -> 0
     * float, double -> 0.0
     * char -> '\u0000'
     * objetos -> null
     */

    // Uma variável local não é inicializada por padrão
    // deve ser inicializada, para não haver erros
    // uma constante também deve ser inicializada
    // variáveis dentro do método main, são locais

    final int i = 0;

    // OBS: o null não aponta para nenhum local de memória
    // dessa forma, ao tentar acessar um atributo/método dessa variável
    // será lançado um erro de tempo de execução
}