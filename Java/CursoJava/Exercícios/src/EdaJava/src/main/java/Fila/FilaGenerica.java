package Fila;

public class FilaGenerica<T> {

    private No refEntradaFila;

    public FilaGenerica(){
        this.refEntradaFila = null;
    }

    public void enqueue(T obj){
        No novoNo = new No(obj);
        novoNo.setRefNo(refEntradaFila);
        refEntradaFila = novoNo;
    }

    public T first(){
        if(!isEmpty()){
            No primeiroNo = refEntradaFila;
            while (true){
                if(primeiroNo.getRefNo() != null){
                    primeiroNo = primeiroNo.getRefNo();
                }else{
                    break;
                }
            }
            return (T) primeiroNo.getObject();
        }
        return null;
    }

    public T dequeue(){
        if(!isEmpty()){
            No primeiroNo = refEntradaFila;
            No noAnterior = refEntradaFila;
            while (true){
                if(primeiroNo.getRefNo() != null){
                    noAnterior = primeiroNo; // lembrar que estamos trabalhando sempre com a referência em memória
                    primeiroNo = primeiroNo.getRefNo();
                }else{
                    noAnterior.setRefNo(null);
                    break;
                }
            }
            return (T) primeiroNo.getObject();
        }
        return null;
    }

    public boolean isEmpty(){
        if(refEntradaFila == null){
            return true;
        }
        return false;
    }

    @Override
    public String toString() {

        No noAux = refEntradaFila;
        String string = "";
        if(refEntradaFila != null){
            while (true){
                string += noAux.getObject() + " ";
                if(noAux.getRefNo() != null){
                    noAux = noAux.getRefNo();
                }else{
                    break;
                }
            }
        }else {
            string += "null";
        }
        return string;
    }
}
