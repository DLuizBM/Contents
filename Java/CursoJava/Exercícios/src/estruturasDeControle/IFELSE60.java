package estruturasDeControle;

import javax.swing.JOptionPane;

public class IFELSE60 {
	public static void main(String[] args) {
		String s = JOptionPane.showInputDialog("Informe o número: ");
		int num = Integer.parseInt(s);
		
		if(num > 7) {
			System.out.println("Aprovado");
		}else {
			System.out.println("Reprovado");

		}
	}
}
