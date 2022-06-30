package OO.Interface161;

public class main {
    public static void main(String[] args) {
        ferrari ferrari = new ferrari(200);
        ferrari.acelerar();
        System.out.println(ferrari.velocidade);

        ferrari.ligarTurbo();
        System.out.println(ferrari.velocidade);
        System.out.println(ferrari.ligarAr);
        ferrari.ligarAr();
        System.out.println(ferrari.ligarAr);
        System.out.println(ferrari.velocidadeAr());
        System.out.println(ferrari.velocidadeCruzeiro());

        int c = 129;
        byte d = (byte) c;
        System.out.println(d);
    }
}