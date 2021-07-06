package ArraysCollections;

import java.util.ArrayDeque;
import java.util.Deque;

public class Pilha128 {

	public static void main(String[] args) {
		Deque<String> livros = new ArrayDeque<>();
		
		// Em pilhas de tamanho definido, se não for mais possível adicionar na pilha
		// add retorna false, push retorna execeção
		livros.add("O pequeno príncipe");
		livros.push("Don Quixote");
		livros.push("O Hobbit");
		
		//LIFO
		// se não existir elementos na pilha
		// peek retorna false, element execeção
		System.out.println(livros.peek());
		System.out.println(livros.element());
		
		// poll remove da pilha e retorna o elemento retirado, se pilha estiver vazia
		// retorna null
		// remove tem o mesmo comportamento, mas se a pilha estiver vazia
		// retorna exceção
		// pop também retorna execeção
		System.out.println(livros.poll());
		System.out.println(livros.remove());
		System.out.println(livros.poll());
		System.out.println(livros.poll());
		System.out.println(livros.pop());


		
	}
}
