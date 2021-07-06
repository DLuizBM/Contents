package Lambdas.InterfacesFuncionais169;

@FunctionalInterface
public interface Calculo {
	
	// método abstrato
	double executar(double a, double b);
	
	default String legal() {
		return "legal";
	}

	default String legal(String a) {
		return a + "legal";
	}
	
	static String massa() {
		return "muito legal";
	}
	
	static String show(){
		return "isso é show";
	}
}