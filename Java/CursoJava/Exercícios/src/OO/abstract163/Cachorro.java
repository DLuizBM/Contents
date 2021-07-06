package OO.abstract163;

public class Cachorro extends Mamifero {
    
    // a classe que extende uma classe abstrata
    // deve implementar o métodos ainda não implementados
    // e pode sobreescrever os métodos concretos
    // como Cachorro herda de mamífero e mamífero de Animal
    // para cachorro será herdado também os métodos ainda não 
    // implementados, sendo assim, na classe cahorro deve-se
    // implementar o mover()(de animal) e o mamar()(de mamífero)
    @Override
    public String mover() {
        return "Se move";
    }

    @Override
    public String mamar() {
        return "Com leite";
    }

}