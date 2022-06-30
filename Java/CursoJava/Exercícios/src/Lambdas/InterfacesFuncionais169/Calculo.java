package Lambdas.InterfacesFuncionais169;

@FunctionalInterface
// Essa annotation não é necessária, ela serva apenas pra mostrar que essa é
// uma interface funcional.
public interface Calculo {
	
	// Interface funcional possui um único método para ser usado no contexto de lambda.
	// A lambda expression só pode ser aplicada usando um único método da interface funcional.
	// A interface funcional pode ter mais de um método, mas deve-se respeitar o fato de que ela
	// só possui um único método abstrato, pois esse é o método que o java vai substituir pela lambda expression.
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