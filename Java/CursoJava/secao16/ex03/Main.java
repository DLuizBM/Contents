package ex03;

public class Main {
    public static void main(String[] args) {
        Elevator elevator = new Elevator(2, 0, 3);
        elevator.getOutOfTheElevator();
        elevator.upFloor();
        System.out.println(elevator.getActualFloor());
        elevator.upFloor();
        System.out.println(elevator.getActualFloor());
        elevator.upFloor();
        elevator.downFloor();
        System.out.println(elevator.getActualFloor());
        elevator.downFloor();
        System.out.println(elevator.getActualFloor());
        elevator.downFloor();
        elevator.getOutOfTheElevator();
        elevator.getOutOfTheElevator();
        elevator.getOutOfTheElevator();
        elevator.getOntheElevator();
        System.out.println(elevator.getActualPeople());
        elevator.getOntheElevator();
        elevator.getOntheElevator();
        System.out.println(elevator.getActualPeople());
        elevator.getOntheElevator();
    }
}
