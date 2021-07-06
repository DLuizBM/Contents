package fundamentos;

public class Wrapper28 {
	public static void main(String [] args) {
		// byte
		Byte b = 100;
		Short s = 1000;
		Integer i = 10000;
		Long l = 100000L; // fazendo conversão direta L-long para long
		
		System.out.println(b.byteValue());
		System.out.println(s.toString());
		
		Boolean bo = Boolean.parseBoolean("true");
		System.out.println(bo);
		System.out.println(bo.toString().toUpperCase());
		
		Float f = 123.0F; // dizendo que é float para fazer a conversão
		double fa = 123.0; // Float é objeto, deve-se fazer a conversão, double tipo primitivo  
		System.out.println(f);
		
	}
}
