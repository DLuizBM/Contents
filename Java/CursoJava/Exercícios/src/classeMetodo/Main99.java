package classeMetodo;

public class Main99 {
	public static void main(String[] args) {
		MembroClass99 area = new MembroClass99();
		
		System.out.println(area.areaCirc(3));
		
		// forma correta de acessar o valor de pi
		MembroClass99.pi = 5;
		area.pi = 10;
		// acessando pela instância de objeto e não de classe, ao mudar o valor de pi
		// todas as instâncias da classe área que usam pi serão alteradas.
		System.out.println(area.areaCirc(3));
		// notar a última alteração em pi é a que vale
		// e será refletido em tudo que usar pi
		
		//Agora com o final static na classe MenmbroClass99
		//Não será mais possível trocar o valor da variável pi
		//MembroClass99.PI = 12;
		
		double raio = 5;
		// chamando o método estático
		System.out.println(MembroClass99.area(raio));
		
	}
}
