public class CastException extends Exception {

    private String nomeDoAtributo;

    public CastException(String nomeDoAtributo){
        this.nomeDoAtributo = nomeDoAtributo;
    }

    public String getMessage(){
        return String.format("A conversão do atributo '%s' está errada", nomeDoAtributo);
    }
}