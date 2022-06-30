package b;
import a.Test;
import a.Test;

class M {
	public static void main(String[] args){
	Test test = new Test();
	/*
	Ao compilar um arquivo, deve-se usar javac e o nome do arquivo, ex: main.java
	Ao executar o arquivo, deve-se usar java e o noma da classe que contém o método main
	Ex: Neste arquivo, o método main está na classe A, logo, para executar deve-se usar java A.
	*/
	System.out.println(test.saudacao() + args[0] + " " + args[1]);
	// Passagem de parâmetro na linha de comando, deve-se executar a classe com o método main e passar
	// todos os parâmetros desejados logo após a classe, separados por espaço. Cada um será uma posição de array.
	// ex: java A Divino Luiz
	System.out.println("Hello ");
	}
}

class B {
	public static void main(String... args){}
}