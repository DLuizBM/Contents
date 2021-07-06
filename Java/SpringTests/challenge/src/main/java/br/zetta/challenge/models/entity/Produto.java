package br.zetta.challenge.models.entity;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;
import javax.persistence.Transient;
import javax.validation.constraints.Max;
import javax.validation.constraints.Min;
import javax.validation.constraints.NotBlank;
@Entity
public class Produto {
	
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY) // essa estratégia gera uma chave de auto incremento
	private int id;
	
	@NotBlank // valida o campo e não deixa que o campo seja vazio
	private String name;
	//@Transient faz com que esse atributo não seja mapeado para o banco de dados
	
	@Min(0)
	@Max(10000) // valida entrada mínima e máxima do preço
	private double preco;
	
	public Produto() {
		// o construtor padrão é necessário para não haver erro
	}
	
	public Produto(String name, double preco) {
		this.name = name;
		this.preco = preco;
	}
	
	public double getPreco() {
		return preco;
	}

	public void setPreco(double preco) {
		this.preco = preco;
	}
	
	public int getId() {
		return id;
	}
	
	public void setId(int id) {
		this.id = id;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}

}
