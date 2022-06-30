package ArraysCollections;

import java.util.LinkedList;
import java.util.Queue;
import java.util.concurrent.ArrayBlockingQueue;
import java.util.concurrent.BlockingQueue;

public class Fila127 {

	public static void main(String[] args) {
		Queue<String> fila = new LinkedList<String>();

		//fila com restrição de tamanho
		BlockingQueue<String> queue = new ArrayBlockingQueue<>(2);
		
		// quando se tem uma fila com restrição de tamanho
		// ao tentar adicionar com o add, se a fila estiver completamente
		// preenchida, ele retorna um erro, lança exceção
		// offer retorna true or false, false se não conseguir adicionar
		fila.add("Ana");
		fila.offer("Bia");
		fila.offer("Carlos");
		fila.offer("Daniel");
		fila.offer("Rafaela");

		queue.add("Abrilina");
		queue.add("Hagar");
		queue.add("Alfafa"); // vai lançar exceção

		for(String name: queue) {
			System.out.println(name);
		}
		
		// Pegando o primeiro elemento da fila
		// comportamento quando a fila está vazia
		// peek retorna nulo caso não consigo pegar um elemento da fila
		// element gera um exceção
		// ambos obtém o elemento, mas não remove da fila
		System.out.println(fila.peek());
		System.out.println(fila.element());
		
		// removendo o primeiro elemento da fila
		// o primeiro que entra é o primeiro que sai
		
		// poll remove e mostra o elemento, se a fila estiver vazia retorna null
		// remove retira da fila e mostra o elemento retirado
		// se fila estiver vazia retorna uma exceção
		System.out.println(fila.poll());
		System.out.println(fila.poll());
		System.out.println(fila.poll());
		System.out.println(fila.remove());

		System.out.println(fila.contains("Rafaela"));
		

	}
}
