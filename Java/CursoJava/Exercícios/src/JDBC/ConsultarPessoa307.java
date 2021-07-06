package JDBC;

import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class ConsultarPessoa307 {
	public static void main(String[] args) throws SQLException{
		Connection conexao = Conexao.getConexao();
		String sql = "SELECT * FROM pessoas";
		
		Statement stmt = conexao.createStatement();
		ResultSet rs = stmt.executeQuery(sql);
		List<Pessoa307> pessoas = new ArrayList<>();

		while(rs.next()) {
			String nome = rs.getString("nome");
			pessoas.add(new Pessoa307(nome));
		}
		
		for(Pessoa307 nome: pessoas) {
			System.out.println(nome.getNome());
		}
		stmt.close();
		conexao.close();
	}
}
