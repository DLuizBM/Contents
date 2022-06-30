public class CadeiaDeException {
    
    public static void main(String[] args){

        Object num = null;
        try{
            metodoA(num);
        }catch (IllegalArgumentException e){
            System.out.println("Causa: " + e.getCause().getMessage()); 
            // ratreando a mensagem que realmente causou o problema.
        }

        metodoA(num);
        // mostrando a StackTrace completa e mostrando que uma execeção é causa de outra.

    }

    static void metodoA(Object num){
        try{
            metodoB(num);
        }catch(Exception causa){
            // causa recebe a exceção NullPointerException
            throw new IllegalArgumentException(causa);
        }
    }

    static void metodoB(Object num){
        if(num == null){
            throw new NullPointerException("O valor é null");
        }
    }

}
