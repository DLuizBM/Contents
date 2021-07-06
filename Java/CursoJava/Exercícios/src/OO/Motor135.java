package OO;

public class Motor135 {

	Carro135 carro;
	boolean ligado = false;
	double fatorInjecao = 1;
	
	
	Motor135(Carro135 carro){
		this.carro = carro;
	}
	
	double giro() {
		if(!ligado) {
			return 0;
		}else {
			return fatorInjecao * 3000;
		}
	}
}
