package OO;

public class CursoTeste137 {
	public static void main(String[] args) {
		
		Aluno137 aluno1 = new Aluno137("João");
		Aluno137 aluno2 = new Aluno137("Maria");

		
		Curso137 curso1 = new Curso137("Java");
		Curso137 curso2 = new Curso137("Python");

		
		aluno1.adicionarCurso(curso1);
		// será adicionado ao array de cursos do aluno1 o curso1
		aluno1.adicionarCurso(curso2);
		curso1.adicionarAlunos(aluno2);
		// será adicionado ao array de alunos do curso1 o aluno2
		
		for(Aluno137 aluno: curso1.alunos) {
			System.out.println(aluno.nome);
		}
		
		System.out.println(aluno1.cursos.get(0).alunos.toString());
		
		// aluno1.obterCurso devolve um objeto do tipo Curso137
		// dessa forma, o único tipo de variável que pode receber esse dado
		// é o tipo Curso137, por isso Curso137 cursoEncontrado
		Curso137 cursoEncontrado = aluno1.obterCurso("Java");
		System.out.println(cursoEncontrado.nome);
		System.out.println(cursoEncontrado.alunos);
	}
}
