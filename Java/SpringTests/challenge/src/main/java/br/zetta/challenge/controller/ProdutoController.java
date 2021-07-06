package br.zetta.challenge.controller;

import java.util.Optional;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.PageRequest;
import org.springframework.data.domain.Pageable;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.bind.annotation.RestController;

import br.zetta.challenge.models.entity.Produto;
import br.zetta.challenge.models.repositories.ProdutoRepository;

@RestController
@RequestMapping("/api/produtos")
public class ProdutoController {
	
	//Injeção de dependências
	@Autowired //com o Autowired, o spring coloca automaticamente um objeto dentro da variável produtoRepository
	private ProdutoRepository produtoRepository;
	/*
	@PostMapping //ResponseBody indica que esse método faz parte do corpo da resposta	
	public @ResponseBody Produto newProduct(@RequestParam String name) { //RequestParam para que o valor passado no post passe para o name
		Produto product = new Produto();
		product.setName(name);
		produtoRepository.save(product);
		return product;
	}
	*/
	//@PostMapping
	//public @ResponseBody Produto newProduct(@Valid Produto product){
		//@Valid, garante que só vai ser passado pra ser inserido se for válido enm conformidade com o que foi feito na classe Produto
		//produtoRepository.save(product);
		//return product;
	//}
	
	@GetMapping
	public Iterable<Produto> getProducts() {
		return produtoRepository.findAll();
	}
	
	@GetMapping(path="/{id}") //Optional, pois pode haver produto ou não nesse Id
	public Optional<Produto> getProduct(@PathVariable int id) { //@PathVariable, variável que está no path da url
		return produtoRepository.findById(id);
	}
	
	@GetMapping(path="/name/{name}") //Optional, pois pode haver produto ou não nesse Id
	public Iterable<Produto> getProductByName(@PathVariable String name) { //@PathVariable, variável que está no path da url
		return produtoRepository.findByNameContaining(name);
		// retunr produtoRepository.searchByNameLike(name);
	}
	
	/*
	@PutMapping
	public Produto updateProduct(@Valid Produto product) {
		produtoRepository.save(product);
		return product;
	}*/
	
	@RequestMapping(method={RequestMethod.POST, RequestMethod.PUT})
	public Produto saveProduct(@Valid Produto product) {
		produtoRepository.save(product);
		return product;
	}
	
	@DeleteMapping(path={"/{id}"})
	public void deleteProduct(@PathVariable int id) {
		produtoRepository.deleteById(id);
	}
	
	@GetMapping(path= {"/paginas/{numeroPagina}/{elementosPorPagina}"})
	public Iterable<Produto> getProductByPages(@PathVariable int numeroPagina, @PathVariable int elementosPorPagina){
		if(elementosPorPagina > 5) elementosPorPagina = 5;
		Pageable page = PageRequest.of(numeroPagina, elementosPorPagina);
		// parâmetros: a página e quantos elementos vem por página
		// a primeira página é a página 0
		return produtoRepository.findAll(page);
	}
}

