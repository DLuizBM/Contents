package ex04;

public class RemoteControl {
    
    Television television;

    public RemoteControl(Television television){
        this.television = television;
    }

    public Television getTelevision(){
        return television;
    }

    public void upChannel(){
        television.upChannel();
    }

    public void downChannel(){
        television.downChannel();
    }

}
