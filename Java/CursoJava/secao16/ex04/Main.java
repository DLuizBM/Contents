package ex04;

public class Main {
    
    public static void main(String[] args) {
        Television television = new Television(100, 0);
        RemoteControl remoteControl = new RemoteControl(television);
        
        System.out.println(remoteControl.getTelevision().getChannel());
        System.out.println(remoteControl.getTelevision().getVolume());
        remoteControl.downChannel();
        remoteControl.downChannel();
        remoteControl.getTelevision().upVolume();
        remoteControl.getTelevision().upVolume();
        System.out.println(remoteControl.getTelevision().getChannel());
        System.out.println(remoteControl.getTelevision().getVolume());
        remoteControl.upChannel();
        remoteControl.getTelevision().downVolume();
        System.out.println(remoteControl.getTelevision().getChannel());
        System.out.println(remoteControl.getTelevision().getVolume());
    }
}
