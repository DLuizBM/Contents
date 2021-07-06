package com.serviceorder.api.controller;

import java.util.Arrays;
import java.util.List;
import java.util.Optional;

import javax.persistence.EntityManager;
import javax.persistence.PersistenceContext;
import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.DeleteMapping;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestController;

import com.serviceorder.domain.model.Client;
import com.serviceorder.domain.model.repository.ClientRepository;


@RestController
@RequestMapping("/clients") // faz com que esse controlador responda sempre nesse endpoint
public class ClientController {
	/*
	@PersistenceContext
	private EntityManager manager;

	@GetMapping("/clients")
	public List<Client> getClients(){
		return manager.createQuery("from Client", Client.class).getResultList();
		// from Client -> jpql
	}
	Essa forma de fazer o controle do banco de dados não é indicada, pois há ligação direta com o EntityManager
	e nem é necessário trabalhar diretamente com jakarta persistence
	*/

	@Autowired
	public ClientRepository clientRepository;

	//@GetMapping("/clients")
	@GetMapping
	public List<Client> getClients(){
		return clientRepository.findAll();
		//return clientRepository.findByName("Abrilina");
	}

	//@GetMapping("/clients/{clientId}")
	@GetMapping("/{clientId}")
	public ResponseEntity<Client> getClient(@PathVariable Long clientId){
		Optional<Client> client = clientRepository.findById(clientId);
		if(client.isPresent())
			return ResponseEntity.ok(client.get());
		return ResponseEntity.notFound().build();
		// se tiver um cliente, retorna status 200 e no corpo da resposta o cliente
		// se não, retorna null e status 404
	}
	

	@PostMapping
	@ResponseStatus(HttpStatus.CREATED) // retorna 201, created
	public Client insertClient(@Valid @RequestBody Client client){ //@Valid é do bean validation @RequestBody, diz para o spring transformar o que vem no post em objeto do tipo Client
		return clientRepository.save(client);
	} 

	@PutMapping("/{clientId}")
	public ResponseEntity<Client> updateClient(@Valid @PathVariable Long clientId, @RequestBody Client client){
		if(!clientRepository.existsById(clientId))
			return ResponseEntity.notFound().build();
		client.setId(clientId);
		client = clientRepository.save(client);
		return ResponseEntity.ok(client);
	}
	
	@DeleteMapping("/{clientId}")
	public ResponseEntity<Void> deleteClient(@PathVariable Long clientId){
		if(!clientRepository.existsById(clientId))
			return ResponseEntity.notFound().build();
		clientRepository.deleteById(clientId); 
		return ResponseEntity.noContent().build(); //noContent, retorna 204, que significa sucesso, porém sem nenhum retorno
	}

}
