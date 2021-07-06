package br.zetta.challenge.controller;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RestController;

@RestController
// annotation para criar uma api do tipo rest
//@RequestMapping(method=RequestMethod.GET, path="/hello") o requestmapping e o getmapping podem estar aqui
//mas por conta da política de cors, eles devem estar no método
public class Controller {
	//mapeando uma requisição para esse método, a convenção padrão é que o request mapping
	//aponta para o método get
	//@RequestMapping(method=RequestMethod.GET, path="/hello")
	@GetMapping(path={"/hello"}) //mapeamento para método específico
	@CrossOrigin(origins="http://localhost:3000")
	public String helloWorld() {
		return "hello world!";
	}
	
}
// o spring por padrão já responde em JSON quando recebe um objeto
// página tutorial de criação e permissão de usuário no mysql 
// https://sempreupdate.com.br/como-criar-um-novo-usuario-e-conceder-permissoes-no-mariadb-e-mysql/
