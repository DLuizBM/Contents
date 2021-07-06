package fundamentos;

public class inferencia20 {
	public static void main(String[] args) {
		double a = 4.5;
		System.out.println(a);
		
		// após declarada uma variável do tipo double, é possível redeclarar como int
		a = 12;
		System.out.println(a);
		
		// colocando var, o java vai inferir o tipo da variável
		// nesse caso, double
		var b = 4.5;
		System.out.println(b);
		
		// após declarar como int, não é posível redeclarar como double
		var c = 10;
		// c = 9.6;
		System.out.println(c);
		
		/*
		 
		 * Tipos primitivos em JAVA
		 * byte - 8 bits
		 * short - 2 bytes
		 * int - 4 bytes
		 * long - 8 bytes
		 * float - 4 bytes
		 * double - 8 bytes
		 * char
		 * boolean
		
		 * */
				
	}

}
