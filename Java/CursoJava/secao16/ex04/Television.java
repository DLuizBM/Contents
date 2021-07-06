package ex04;

public class Television {
    
    private int channel;
    private int volume;

    public Television(int channel, int volume){
        this.channel = channel;
        this.volume = volume;
    }

    public int getChannel(){
        return channel;
    }

    public int getVolume(){
        return volume;
    }

    public void upChannel(){
        this.channel += 1;
    }

    public void downChannel(){
        this.channel -= 1;
    }

    public void upVolume(){
        this.volume += 1;
    }

    public void downVolume(){
        this.volume -= 1;
    }

}
