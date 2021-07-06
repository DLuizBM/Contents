package classeMetodo;

public class Data92 {
	
	String dataFormatada(String dia, String mes, String ano) {
		return dia+"/"+mes+"/"+ano;
	}
	String dataFormatada() {
		return String.format("olá mundo!!");
		// esse método é mais interessante do que usar Sytem.out.println
		// ao retornar a string é possível usar em aplicações desktop
		// web e mobile, enquanto que system.out.println só roda em terminal
	}
	
	
}