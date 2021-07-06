package JDBC;

import java.sql.Connection;
import java.sql.SQLException;

import java.sql.PreparedStatement;

public class Inserir306 {
	public static void main(String[] args) throws SQLException{
		Connection conexao = Conexao.getConexao();
		
		// VALUES com interrogação é para evitar sql injections que podem
		// danificar o banco
		// dessa forma, deve-se passar o valor desejado como parâmetro
		// com o PrepareStatement
		String nome = "Divino";
		String sql = "INSERT INTO pessoas (nome) VALUES (?)";
		PreparedStatement stmt = conexao.prepareStatement(sql);
		stmt.setString(1, nome);
		// para usar o preparedStatement deve-se usar o set, no caso de string
		// setString, 1 indica qual parâmetro vai receber a string, nome indica string 
		// passada
		
		stmt.execute();
		
		System.out.println("Pessoa incluída com sucesso");
	}	
}
