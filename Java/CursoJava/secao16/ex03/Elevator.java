package ex03;

public class Elevator extends PrimitiveElevator implements interfaceElevator {
    
    private int actualPeople;

    public Elevator(int totalFloors, int actualFloor, int capacity){
        super(totalFloors, actualFloor, capacity);
        this.actualPeople = capacity;
    }

    public int getTotalFloors(){
        return totalFloors;
    }

    public int getCapacity(){
        return capacity;
    }

    public int getActualFloor(){
        return actualFloor;
    }

    public int getActualPeople(){
        return actualPeople;
    }

    public void getOntheElevator(){
        if((actualPeople + addPerson()) <= capacity){
            actualPeople += addPerson();
        }else{
            System.out.println(toString());
        }
    }

    public void getOutOfTheElevator(){
        if((actualPeople + takeOffPerson()) >= 0){
            actualPeople += takeOffPerson();
        }else{
            System.out.println("There are no people in the elevator.");
        }
    }

    public void upFloor() {
        if((getActualFloor() + up()) <= totalFloors){
            actualFloor += up();
        }else{
            System.out.println("Elevator is on the top floor.");
        }        
    }

    public void downFloor() {
        if((getActualFloor() + down()) >= 0){
            actualFloor += down();
        }else{
            System.out.println("Elevator is on the ground floor.");
        } 
    }

    @Override
    public String toString(){
        return "Exceeded capacity people.";
    }

}
