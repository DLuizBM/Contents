package br.zetta.challenge.models.repositories;

import org.springframework.data.repository.CrudRepository;

import br.zetta.challenge.models.entity.JobPosition;

public interface JobPositionRepository extends CrudRepository<JobPosition, Integer> {

}
