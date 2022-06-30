package Pilha;

public class Main {

    public static void main(String[] args) {
        Pilha myStack = new Pilha();
        myStack.push(new No(1));
        myStack.push(new No(2));
        myStack.push(new No(3));
        myStack.push(new No(4));

        System.out.println(myStack);
        System.out.println(myStack.pop());
        System.out.println(myStack);

    }
}
