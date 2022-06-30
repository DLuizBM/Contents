import java.util.Scanner;

public class Finally {

    public static void main(String[] args){
        
        Scanner s = new Scanner(System.in);
        int num = s.nextInt();

        // Esse programinha simula um exemplo em que independente de erro ou não
        // Algo deve ser feito, o finally faz isso. Imagine uma operação em um banco de dados que gere um erro.
        // Mesmo a operação não dando certo, é necessário finalizar a conexão com o banco.
        
        try {
            System.out.println(7 / num);
        }catch (Exception e){
            System.out.println("Erro:" + e.getMessage());
        }finally {
            System.out.println("Finalizando conexão");
            s.close();
        }
        System.out.println("Fim");
    }
    
}
