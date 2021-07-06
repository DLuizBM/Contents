package JDBC;

import java.sql.Connection;
import java.sql.Statement;

public class CriarTabela {
	public static void main(String[] args) throws Exception {
		
		Connection conexao = Conexao.getConexao();
		
		String sql = "CREATE TABLE IF NOT EXISTS pessoas ("
				+ "codigo INT AUTO_INCREMENT PRIMARY KEY,"
				+ "nome VARCHAR(80) NOT NULL" // não pode ter vírgula no último campo da tabela
				+ ")";
		
		Statement stmt = conexao.createStatement();
		stmt.execute(sql);
		conexao.close();
		
	}
}
