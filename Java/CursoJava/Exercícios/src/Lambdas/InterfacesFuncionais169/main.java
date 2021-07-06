package Lambdas.InterfacesFuncionais169;

public class main {
	 public static void main(String[] args) {
		 
		 Calculo calc;
		 calc = (x, y) -> { // implementando o único método abstrato que existe na interface funcional,
			 return x + y ; // dessa forma, essa função vai representar a implentação do método executar
		 };
		 System.out.println(calc.executar(1, 2));
		 System.out.println(calc.legal());
		 System.out.println(Calculo.massa());
		 // acesso ao método estático, pois é um método de classe
		 // o método estático não possui o this, que é a instância atual
		 // a partir de um membro de instância é possível acessar os membros
		 // estáticos
		 System.out.println(new main().helloWord());
		 
	}

	public String helloWord(){
		return "Hello " + happy() + " World";
	}

	private String happy(){
		return "happyyy";
	}
}
