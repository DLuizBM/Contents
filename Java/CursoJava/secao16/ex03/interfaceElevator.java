package ex03;

public interface interfaceElevator {
    
    default int addPerson(){
        return 1;
    }

    default int takeOffPerson(){
        return -1;
    }

    default int up(){
        return 1;
    }

    default int down(){
        return -1;
    }
}
