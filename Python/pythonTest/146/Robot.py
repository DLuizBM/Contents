class Robot:

    def __init__(self, name, battery=100, skills=[]):
        self.__name = name
        self.__battery = battery
        self.__skills = skills
    
    @property
    def name(self):
        return self.__name
    
    @property
    def battery(self):
        return self.__battery
    
    @property
    def skills(self):
        return self.__skills
    
    def charge(self):
        self.__battery = 100
    
    def say_name(self):
        if self.__battery > 0:
            self.__battery -= 1
            return f"Oi, eu sou o robô {self.__name}."
        return f"Bateria fraca."
    
    def learn_skill(self, new_skill, loss_battery):
        if self.__battery >= loss_battery:
            self.__battery -= loss_battery
            self.__skills.append(new_skill)
            return f"Eu aprendi a seguinte habilidade: {new_skill}."
        return f"Bateria insuficiente."