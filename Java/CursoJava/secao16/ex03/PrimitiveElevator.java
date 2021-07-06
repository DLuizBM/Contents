package ex03;

public abstract class PrimitiveElevator {
    
    protected int totalFloors;
    protected int capacity;
    protected int actualFloor;

    public PrimitiveElevator(int totalFloors, int actualFloor, int capacity){
        this.totalFloors = totalFloors;
        this.actualFloor = actualFloor;
        this.capacity = capacity;
    }

    public abstract int getTotalFloors();
    public abstract int getCapacity();
    public abstract void upFloor();
    public abstract void downFloor(); 
}
