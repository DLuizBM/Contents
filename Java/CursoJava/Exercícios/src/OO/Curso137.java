package OO;

import java.util.ArrayList;

public class Curso137 {

	final String nome;
	final ArrayList<Aluno137> alunos = new ArrayList<Aluno137>();
	
	Curso137(String nome){
		this.nome = nome;
	}
	
	// relação bidirecional
	
	void adicionarAlunos(Aluno137 aluno) {
		this.alunos.add(aluno);
		aluno.cursos.add(this);
		System.out.println("Adicionar Alunos " + this);

	}
	
	
}
