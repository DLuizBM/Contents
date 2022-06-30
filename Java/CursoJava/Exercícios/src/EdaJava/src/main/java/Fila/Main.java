package Fila;

public class Main {

    public static void main(String[] args){

        // Versão 1

        Fila fila = new Fila();

        fila.enqueue(new No("primeiro"));
        fila.enqueue(new No("segundo"));
        fila.enqueue(new No("terceiro"));
        fila.enqueue(new No("quarto"));

        System.out.println(fila);

        System.out.println(fila.dequeue());

        System.out.println(fila.first());

        // Versão 2

        FilaRefatorada filaRefatorada = new FilaRefatorada();
        filaRefatorada.enqueue("primeiro");
        filaRefatorada.enqueue("segundo");
        filaRefatorada.enqueue("terceiro");
        filaRefatorada.enqueue("quarto");

        System.out.println(filaRefatorada);
        System.out.println(filaRefatorada.dequeue());
        System.out.println(filaRefatorada.first());

        // Versão 3

        FilaGenerica<String> filaGenerica = new FilaGenerica<String>();
        filaGenerica.enqueue("primeiros");
        filaGenerica.enqueue("segundo");
        filaGenerica.enqueue("terceiro");
        filaGenerica.enqueue("quarto");

        System.out.println(filaGenerica);
        System.out.println(filaGenerica.dequeue());
        System.out.println(filaGenerica.first());

    }

}
