package OO;

public class Carro135 {
	
	Motor135 motor;
	
	Carro135(){
		// o próprio objeto atual é o carro que vou passar para construir o motor
		// relação bidirecional
		this.motor = new Motor135(this);
		System.out.println(this);
	}
	
	void acelerar() {
		motor.fatorInjecao += 0.4;
	}
	
	void frear() {
		motor.fatorInjecao -= 0.4;
	}
	
	void ligar() {
		motor.ligado = true;
	}
	
	void desligar() {
		motor.ligado = false;
	}

	boolean estaLigado() {
		return motor.ligado;
	}
}
