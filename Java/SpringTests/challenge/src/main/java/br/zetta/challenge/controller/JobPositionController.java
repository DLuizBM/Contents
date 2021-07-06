package br.zetta.challenge.controller;

import javax.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import br.zetta.challenge.models.entity.JobPosition;
import br.zetta.challenge.models.repositories.JobPositionRepository;

@RestController
@RequestMapping("/job_position")
public class JobPositionController {
	
	@Autowired
	private JobPositionRepository jobPositionRepository;
	
	@GetMapping
	public Iterable<JobPosition> getJobPositions() {
		return jobPositionRepository.findAll();
	}
	
	@PostMapping
	public JobPosition insertJobPosition(@RequestBody JobPosition jobPosition) {
		System.out.println(jobPosition.getName());
		jobPositionRepository.save(jobPosition);
		return jobPosition;
	}

}
