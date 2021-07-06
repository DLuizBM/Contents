package com.serviceorder.domain.model.repository;

import java.util.List;

import com.serviceorder.domain.model.Client;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;


@Repository
public interface ClientRepository extends JpaRepository<Client, Long> { //<Client(Entidade), Long(tipo do identificador, id em Client é Long)>
    
    List<Client> findByName(String name);
    List<Client> findByNameContaining(String name);
    // escrevendo métodos específicos, deve-se usar findByNOMEDOATRIBUTO

}
