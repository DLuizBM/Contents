package com.serviceorder.api.exceptionHandler;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Locale;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.MessageSource;
import org.springframework.context.i18n.LocaleContextHolder;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.validation.FieldError;
import org.springframework.validation.ObjectError;
import org.springframework.web.bind.MethodArgumentNotValidException;
import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.context.request.WebRequest;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@ControllerAdvice //componente do spring que diz que as exceptions dos controladores vão ser tratadas por essa classe
				  // se alguma exception acontecer em algum controlador, cai aqui 
public class ApiExceptionHandler extends ResponseEntityExceptionHandler{
    
	/*
	 * O único tipo de exception que essa classe está tratando(devolve uma mensagem customizada) é o MethodArgumentNotValid, pois somente 
	 * o método handleMethodArgumentNotValid foi sobrescrito. Dentro de ResponseEntityExceptionHandle há outros tipos de métodos tratando
	 * outras exceptions, caso se queira tratar outros tipos de exceptions, basta sobrescrever outro métodos
	 * 
	 */
	
	@Autowired
	private MessageSource messageSource;
	
    @Override
    protected ResponseEntity<Object> handleMethodArgumentNotValid(MethodArgumentNotValidException ex,
            HttpHeaders headers, HttpStatus status, WebRequest request) {
        // TODO Auto-generated method stub
    	
    	Exception exception = new Exception(); // essa classe representa o que quero na resposta, nesse caso (status, título, hora e campos)

    	var campos = new ArrayList<Exception.Campo>();
    	for(ObjectError error: ex.getBindingResult().getAllErrors()) {
    		String name = ((FieldError)error).getField();
    		//String message = error.getDefaultMessage();
    		String message = messageSource.getMessage(error, LocaleContextHolder.getLocale()); // para buscar a mensagem no message.properties
    		campos.add(new Exception.Campo(name, message));
    	}
    	
        exception.setStatus(status.value());
        exception.setTitle("Um ou mais campos estão inválidos. Preencha todos corretamente.");
        exception.setDateHour(LocalDateTime.now());
        exception.setCampos(campos);
        //return super.handleMethodArgumentNotValid(ex, headers, status, request); mudar para
        return super.handleExceptionInternal(ex, exception, headers, status, request);
    }
    
    /*
     * Quando um exception é resolvida, o spring gera alguns codes(ex: NotBlank) que podem ser usado para
     * traduzir mensagens. Para isso, é necessário criar um arquivo messages.properties em resources.
     * Deve ainda injetar o MessageSource
     * vídeo 1:30
     */
}
