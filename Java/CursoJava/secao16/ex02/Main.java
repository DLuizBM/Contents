package ex02;

public class Main {
    
    public static void main(String[] args) {

        person goku = new person("Goku", "45", "1.75");
        person vegeta = new person("Vegeta", "46", "1.70");

        control control = new control();

        control.addPerson(goku);
        control.addPerson(vegeta);

        System.out.println(control.searchPerson(goku.getName()));
        control.printPerson(0);
        control.printNotebook();
        control.removePerson(goku.getName());
        System.out.println("Após remover " + goku.getName());
        control.printNotebook();
        
    }
}
