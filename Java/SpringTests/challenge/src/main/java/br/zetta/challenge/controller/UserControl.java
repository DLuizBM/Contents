package br.zetta.challenge.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import br.zetta.challenge.models.entity.Model;

@RestController
@RequestMapping("/users")
public class UserControl {
	
	// por conta do cors o GetMapping e o CrossOrigin devem estar no método
	@GetMapping(path="/all")
	@CrossOrigin(origins="http://localhost:3000")
	public Model getUser() {
		return new Model(1, "Zetta");
	}
	
	@GetMapping("/{id}") // a url para acessar esse método será /users/id
	public Model getUserById(@PathVariable int id) { //para que o valor de {id} seja passado para id é necessário @PathVariable
		return new Model(id, "Maria");
	}
	
	@GetMapping
	public Model getUserById2( // segunda forma de passar parâmetros para o webService, forma de chamar http://localhost:8080/users?id=10
			@RequestParam(name="id", defaultValue="1") int id) {
		return new Model(id, "João");
	}
	
	@GetMapping("/calc/{n1}/{n2}") //http://localhost:8080/users/calc/10/20
	public int calc1(@PathVariable int n1, @PathVariable int n2) {
		return n1 + n2;
	}
	
	@GetMapping("/calc") //http://localhost:8080/users/calc?n1=10&n2=12
	public int calc2(@RequestParam(name="n1") int n1, @RequestParam(name="n2") int n2) {
		return n1 + n2;
	}

}
