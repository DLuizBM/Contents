package OO;

public class CarroTeste135 {

	public static void main(String[] args) {
		Carro135 c1 = new Carro135();
		System.out.println(c1);
		System.out.println(c1.estaLigado());
		c1.ligar();
		System.out.println(c1.motor.giro());
		
		c1.acelerar();
		c1.acelerar();
		System.out.println(c1.motor.giro());
	}
}
