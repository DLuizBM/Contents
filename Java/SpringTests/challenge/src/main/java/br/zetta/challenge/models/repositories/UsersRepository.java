package br.zetta.challenge.models.repositories;

import org.springframework.data.repository.CrudRepository;

import br.zetta.challenge.models.entity.Users;

public interface UsersRepository extends CrudRepository<Users, Integer> {

}
