package fundamentos;

public class Ternario {
	// args são argumentos que são passados via terminal do computador
	// quando se roda um arquivo java pelo terminal
	public static void main(String[] args) {
		double media = 7.0;
		
		String nota = media >= 7 ? "Aprovado" : "Reprovado";
		
		System.out.println(nota);
	}
}
