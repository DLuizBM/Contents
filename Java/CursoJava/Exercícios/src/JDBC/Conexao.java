package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

import javax.management.RuntimeErrorException;

public class Conexao {
	public static Connection getConexao() {
		try {
			
			final String stringDeConexao = "jdbc:mysql://localhost/curso_java?verifyServerCertificate=false&useSSL=true";
		    final String usuario = "root";
		    final String senha = "Info@1234";
		    return DriverManager.getConnection(stringDeConexao, usuario, senha);

		}catch(SQLException e){
			throw new RuntimeException(e);
		}
	}
}
