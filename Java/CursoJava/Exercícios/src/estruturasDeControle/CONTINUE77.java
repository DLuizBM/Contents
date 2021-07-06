package estruturasDeControle;

public class CONTINUE77 {
	public static void main(String[] args) {
		for(int i = 0; i < 10; i++) {
			if(i % 2 == 1) {
				continue;
				// continue interrompe apenas a iteração e não todo o laço
				// indo imediatamente para a próxima
				// olhar o continue rotulado
			}
			System.out.println(i);
		}
	}
}
