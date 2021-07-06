package classeMetodo;

public class MembroClass99 {
	
	double area;
	static double pi = 3.14;
	
	// final é usado para definir uma constante, sendo impossível alterar o valor 
	final static double PI = 3.1415;
	// fixando pi como uma variável de classe
	// sendo assim se pi for mudado em outra classe
	// o valor vai se refletir de forma global
	// alterando o valor de pi em todas as classes e métodos que usam pi
	
	double areaCirc(double raio){
		area = pi * raio * raio;
		return area;
	}
	double areaCirc2(double raio) {
		area = PI * raio * raio;
		return area;
	}
	
	// O método estático será um método de instância de classe
	static double area(double raio) {
		return PI * raio * raio;
	}
}
