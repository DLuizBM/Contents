package Lambdas;

public class Soma167 implements Calculo167 {

		@Override
		public double executar(double a, double b) {
			return a + b + 3;
		}

		public double somaDobrado(double a, double b){
			return 2 * (a + b);
		}
}
