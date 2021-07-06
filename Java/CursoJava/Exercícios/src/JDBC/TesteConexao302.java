package JDBC;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class TesteConexao302 {

    public static void main(String[] args) throws SQLException {
    // se acontecer uma exceção, vai simplesmente sair do main com erro    
    
    // o jdb precisa de uma string de conexão
    // é um string suportada pelo driver do jdbc
    final String stringDeConexao = "jdbc:mysql://localhost?verifyServerCertificate=false&useSSL=true";
    final String usuario = "root";
    final String senha = "Info@1234";

    // Para criar a conexão deve-se importar o connection

    Connection conexao = DriverManager
    .getConnection(stringDeConexao, usuario, senha);
    // o DriverManager é um método que lança uma exceção checada
    // uma execeção checada precisa ser tratada
    // pode-se tratar com try catch ou lançar(throw) e deixar outro cara tratar
    System.out.println("Conexão efetuada com sucesso.");
    conexao.close();
  }
}