package Pilha;

public class Pilha {

    private No noRefEntradaPilha;

    public Pilha() {
        this.noRefEntradaPilha = null;
    }

    public boolean isEmpty(){
        return noRefEntradaPilha == null ? true : false;
    }

    public No top(){
        return noRefEntradaPilha;
    }

    public void push(No novoNo){
        No aux = noRefEntradaPilha;
        noRefEntradaPilha = novoNo;
        noRefEntradaPilha.setNoRef(aux);
    }

    public No pop(){
        if(!isEmpty()){
            No noPoped = noRefEntradaPilha;
            noRefEntradaPilha = noRefEntradaPilha.getNoRef();
            return noPoped;
        }
        return null;
    }

    @Override
    public String toString(){

        No noRef = noRefEntradaPilha;
        String string = "";
        while(true){
            if(noRef != null){
                string += noRef.getDado() + " ";
                noRef = noRef.getNoRef();
            }else{
                break;
            }
        }
        return string;
    }
}
