package Lambdas.forEach171;

import java.util.Arrays;
import java.util.List;

public class Aprovados {

		public static void main(String[] args) {
			List<String> aprovados = Arrays.asList("Ana", "Bia", "Lia", "Gui");
			
			aprovados.forEach((nome) -> {
				System.out.println(nome);
			});
			
			aprovados.forEach(nome -> System.out.println(nome));
			
			System.out.println("Method reference");
			aprovados.forEach(name -> show(name));
			aprovados.forEach(System.out::println);
			aprovados.forEach(Aprovados::show);
			aprovados.forEach(Aprovados::congratulations);
			//a sintaxe para usar o method reference
			//classe(Aprovados)::função

		}
		
		static void show(String name) {
			System.out.println(name);
		}

		static void congratulations(String name) {
			System.out.println("Congratulations " + name + ", you have been aproved.");
		}
}
