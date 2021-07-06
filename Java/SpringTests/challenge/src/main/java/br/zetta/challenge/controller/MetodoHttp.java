package br.zetta.challenge.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PatchMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
@RequestMapping("/methods")
//dessa forma, todos os métodos vão responder na mesma url, o que diferencia é a 
//annotation de cada um para diferenciar o método, por padrão chama o método GET
public class MetodoHttp {
	
	@GetMapping
	public String get() {
		return "Requsição GET";
	}
	
	@PostMapping
	@CrossOrigin(origins="http://localhost:3000")
	public String post() {
		System.out.println("Requisição POST");
		return "Requsição POST";
	}
	
	@PutMapping
	@CrossOrigin(origins="http://localhost:3000")
	public String put() {
		return "Requsição PUT";
	}
	
	@DeleteMapping
	public String delete() {
		return "Requsição DELETE";
	}
	
	@PatchMapping
	public String patch() {
		return "Requsição PATCH";
	}

}
