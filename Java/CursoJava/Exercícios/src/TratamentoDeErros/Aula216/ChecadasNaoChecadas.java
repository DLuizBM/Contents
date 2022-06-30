public class ChecadasNaoChecadas {

    public static void main(String[] args) throws Exception {
        
        geraErro1();

        try{
            geraErro2();
        }catch(Throwable e){
            // tudo que é Thrwable pode ser lançado
            System.out.println("Erro 2 executado");
        }

        geraErro3();
        System.out.println("Fim");

        geraErro4();

    }

    // Unchecked exception: Utilizada para erros irrecuperáveis, ou seja, o erro não pode ser tratado. Ex, nullPointerException, não é obrigatório tratá-las
    // Herda de runtimeException, ex: NullPointerException, NumberFormatException, ClassCastExceprion, etc.
    static void geraErro1(){
        throw new RuntimeException("Ocorreu um erro 1"); // lance um novo erro do tipo RuntimeException
        //throw lança o erro

    }

    // Checked exception: Utilizada para erros recuperáveis, ou seja, quando o erro pode ser tratado. É obrigatório tratá-las
    // herda direto de exception, ex:IOException, SQLException, etc.
    // na exceção checada é obrigatório a dizer na assinatura do método que uma execeção será lançada, utilizando thrwos, ou fazer o tratamento direto no método.
    // O throws joga o tratamento do erro para a chamada do método, ou seja, a exception é lançada no método main.
    static void geraErro2() throws Exception{
        throw new Exception("Ocorreru um erro 2");
    }

    static void geraErro3(){
        try{
            throw new Exception("Ocorreru um erro 3");	
        }catch(Exception e){
            System.out.println("Erro 3 executado");
        }
    }

    // No geraErro4, foi utilizado throw para jogar a exceção para onde o método foi chamado, esperando que lá ela seja tratada
    // porém, o local onde o método é chamado, linha 16, não está se responsabilizando pelo tratamento da exception, passando essa responsabilidade
    // para o método main dizer ao próximo método que o está chamando tratar a exception, porém o método main é o último método da StackTrace, sendo assim,
    // o programa termina de forma abrupta 
    static void geraErro4() throws Exception{
        throw new Exception("Ocorreru um erro 4");	

    }
    
}
