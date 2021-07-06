package com.serviceorder.api.exceptionHandler;

import java.time.LocalDateTime;
import java.util.List;

public class Exception {
    
    private Integer status;
    private String title;
    private LocalDateTime dateHour;
    private List<Campo> campos;
    
    public static class Campo {
    	
    	private String name;
    	private String message;
    	
		public Campo(String name, String message) {
			super();
			this.name = name;
			this.message = message;
		}

		public String getName() {
			return name;
		}
		
		public void setName(String name) {
			this.name = name;
		}
		
		public String getMessage() {
			return message;
		}
		
		public void setMessage(String message) {
			this.message = message;
		}
    	
    }

    public Integer getStatus() {
        return status;
    }

    public void setStatus(Integer status) {
        this.status = status;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public LocalDateTime getDateHour() {
        return dateHour;
    }

    public void setDateHour(LocalDateTime dateHour) {
        this.dateHour = dateHour;
    }

	public List<Campo> getCampos() {
		return campos;
	}

	public void setCampos(List<Campo> campos) {
		this.campos = campos;
	}
    
}

