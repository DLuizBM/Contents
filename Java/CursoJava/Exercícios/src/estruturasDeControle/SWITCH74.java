package estruturasDeControle;

public class SWITCH74 {
	public static void main(String [] args) {
		String time = "Botafogo";
		
		switch(time) {
		case "Flamengo":
			System.out.println("Melhor time");
			break;
			// break é usado para interromper o fluxo do código, pode ser usado em laços 
			// de repetição	
		case "Vasco": case "Botafogo":
			System.out.println("Freguês");
			break;
			// olhar o break rotulado
		default:
			System.out.println("Você não tem time.");
		}
	}
}
