package Fila;

public class NoRefatorado<T> {

    private T object;
    private NoRefatorado<T> refNo;

    public NoRefatorado(){}

    public NoRefatorado(T object){
        this.refNo = null;
        this.object = object;
    }

    public Object getObject() {
        return object;
    }

    public void setObject(T object) {
        this.object = object;
    }

    public NoRefatorado getRefNo() {
        return refNo;
    }

    public void setRefNo(NoRefatorado refNo) {
        this.refNo = refNo;
    }

    @Override
    public String toString() {
        return "No{" +
                "object=" + object +
                '}';
    }

}
