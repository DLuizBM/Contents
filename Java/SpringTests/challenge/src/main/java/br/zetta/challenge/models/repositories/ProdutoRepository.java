package br.zetta.challenge.models.repositories;

import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.PagingAndSortingRepository;
import br.zetta.challenge.models.entity.Produto;

// interface responsável por fazer a persistência de dados
//public interface ProdutoRepository extends CrudRepository<Produto, Integer> {

//}
// Crud repository é o mais simples para se trabalhar. PagingAndSortingRepository, fornece as funções do crud e outras
public interface ProdutoRepository extends PagingAndSortingRepository<Produto, Integer> {
	
	public Iterable<Produto> findByNameContaining(String name);
	// o spring usa uma série de conveções para fazer busca, com o método acima ele já consegue buscar um Produto pelo nome.
	// Ele já gera a sql que vai fazer essa busca. Para implementar métodos como esse, basta seguir a convenção
	// findByNomeDesejadoContaining
	
	/*
	 * @Query("SELECT p FROM Produto p Where p.nome LIKE %:nome%")
	 * 	public Iterable<Produto> searchByNameLike(@Param("nome") String nome);

	 * */

}

