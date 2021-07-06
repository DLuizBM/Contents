package OO.abstract163;

public class main {
    
    public static void main(String[] args) {
        
        Animal cachorro = new Cachorro();
        // cachorro é a única classe concreta
        // sendo assim, a única a que pode ser instanciada
        // ao instaciar como Animal, não se tem acesso ao método mamar
        // pois esse método é de cachorro e não de Animal
        // Quero criar um cachorro sendo um animal, logo, para saber 
        // os métodos disponíveis para cachorro, devo ver os métodos disponíveis
        // na classe Animal e não na Classe Cachorro
        
        System.out.println(cachorro.respirar());
        Cachorro dog = new Cachorro();
        System.out.println(dog.mamar());

        Mamifero cachorroLoko = new Cachorro();
        System.out.println(cachorroLoko.mamar());
        System.out.println(cachorroLoko.mover());
        System.out.println(cachorroLoko.respirar());

        // instanciando cachorro como mamífero, além dos métodos
        // da classe animal, o objeto terá também os métodos da classe
        // mamífero
        

    }
}