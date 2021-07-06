package ex02;

import java.util.ArrayList;
import java.util.List;


public class control implements peopleinterface {
    
    private List<person> peopleList = new ArrayList<>(10);

    public control(){

    }

    public void addPerson(person person){
        peopleList.add(person);
    }

    public void removePerson(String thePerson){
        for(person person: peopleList){
            if(person.getName().equalsIgnoreCase(thePerson)){
                peopleList.remove(person);
            }
        }
    }

    public int searchPerson(String thePerson){
        int index = 11;
        for(person person: peopleList){
            if(person.getName().equalsIgnoreCase(thePerson)){
                index = peopleList.indexOf(person);
            }
        }
        return index;
    }

    public void printNotebook(){
        for(person person: peopleList){
            System.out.println(person.getName());
            System.out.println(person.getAge());
            System.out.println(person.getHeigth());
        }
    }

    public void printPerson(int index){
        System.out.println(peopleList.get(index).getName());
        System.out.println(peopleList.get(index).getAge());
        System.out.println(peopleList.get(index).getHeigth());
    }

}
