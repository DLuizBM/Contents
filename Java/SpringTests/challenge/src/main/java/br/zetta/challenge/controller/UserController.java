package br.zetta.challenge.controller;

import javax.validation.Valid;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.zetta.challenge.models.entity.Users;
import br.zetta.challenge.models.repositories.UsersRepository;

@RestController
@RequestMapping("/users")
public class UserController {
	
	@Autowired
	private UsersRepository usersRepository;
	
	@PostMapping
	public Users insertUser(@RequestBody Users user) {
		System.out.println(user.getJobPosition());
		usersRepository.save(user);
		return user;
	}

}
