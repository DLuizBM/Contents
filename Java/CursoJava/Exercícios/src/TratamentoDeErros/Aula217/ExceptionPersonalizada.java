public class ExceptionPersonalizada {
    public static void main(String[] args) {

        int num = -7;

        Object num2 = 10.1;

        
        //try{
            verifyNumber(num);  // com apenas essa linha, o programa está apenas lançando a exception(mensagem padrão de exception)
                                // com try e catch a exception está sendo tratada, continuando e fluxo do programa e colocando a mensagem do System.out
        //}catch(NumeroNegativoException e){
        //    System.out.println("Erro: " + e.getMessage());
        //}

        try{
            castConversion(num2);
        }catch(CastException e){
            System.out.println("Erro: " + e.getMessage());
        }

        
    }

    //Unchecked exception
    static void verifyNumber(int num){
        if(num < 0){
            throw new NumeroNegativoException("num");
        } 
    }

    //Checked exception
    static void castConversion(Object num) throws CastException{
        if(num.getClass() != Integer.class){
            throw new CastException("num");
        }else{
            System.out.println("É possível fazer a conversão para Integer");
        }
    }
}
