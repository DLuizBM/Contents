package Aula1;
//214
public class Basic {

    public static void main(String[]args){

        try{
            System.out.println("Divisão " + 7 / 0);
        }catch(ArithmeticException e){
            System.out.println(e.getStackTrace()); //printa toda a pilha de execução até o erro.
            System.out.println("Um problema ocorreu " + e.getMessage());
        }
    }
}