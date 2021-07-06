package ex02;

public class person {
    private String name;
    private String age;
    private String heigth;

    public person(String name, String age, String heigth){
        this.name = name;
        this.age = age;
        this.heigth = heigth;
    }

    public String getName(){
        return name;
    }

    public String getAge(){
        return age;
    }

    public String getHeigth(){
        return heigth;
    }

    public void setName(String name){
        this.name = name;
    }

    public void setAge(String age){
        this.age = age;
    }

    public void setHeigth(String heigth){
        this.heigth = heigth;
    }
}
