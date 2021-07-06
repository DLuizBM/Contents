package OO;

import java.util.ArrayList;

public class Aluno137 {

	final String nome;
	final ArrayList<Curso137> cursos = new ArrayList<Curso137>();
	// final em ArrayList, significa que o endereço de memória desse objeto é constante
	// não pode ser modificado, mas o conteúdo da lista é variável
	
	Aluno137(String nome){
		this.nome = nome;
	}
	
	//lembrando que, um aluno terá um array de cursos
	// e um curso terá um array de alunos
	// relação muitos para muitos, pois um aluno pode ter vários cursos
	// e um curso ter vários alunos
	void adicionarCurso(Curso137 curso) {
		this.cursos.add(curso);
		// this representa o aluno, ou seja, o objeto atual que está manipulando esse método
		// será adicionado um curso ao array de cursos do objeto 
		curso.alunos.add(this);
		// será adicionado um aluno(this) ao array de alunos daquele curso
		System.out.println("Adicionar Curso " + this);
	}
	
	public String toString() {
		return nome;
	}
	
	Curso137 obterCurso(String nome) {
		for(Curso137 curso: this.cursos) {
			if(curso.nome.equalsIgnoreCase(nome)) {
				return curso;
			}
		}
		return null;	
	}
}
