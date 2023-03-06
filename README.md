<img src="banner.png" alt="banner">

## **Oi! Me chamo Nícolas** 👋🏼👨🏼‍💻

Sou um **Desenvolvedor Backend** 👨🏼‍💻 apaixonado por resolver problemas, criar soluções inovadoras e por tornar a contribuição para o código aberto mais acessível :rocket:, criando tecnologia para elevar as pessoas! Algumas tecnologias com as quais gosto de trabalhar incluem **Django**:snake:, **Flask**:hot_pepper:, **FastAPI**:zap:, **Express** e **Spring Framework**:coffee: de Frameworks, e com **Oracle Database**, **PostgreSQL**:elephant:, **MySQL**:whale: e **Redis**.

:pushpin: Explore meu [**portfólio de projetos em Python**](https://github.com/Nicolas-albu/Portfolio-Python), onde utilizei os frameworks **Django**:snake:, **FastAPI**:zap: e **Flask**:hot_pepper: para desenvolver soluções web robustas e escaláveis!:rocket: Conheça as aplicações que construí e como elas podem agregar **valor ao seu negócio**:money_with_wings:. Acesse agora e **descubra como posso ajudá-lo a transformar suas ideias:bulb: em realidade!:dart:**

##

<div align="center" alt="contacts">
  <a href="https://instagram.com/nicolas.albu" target="_blank"><img src="https://img.shields.io/badge/Instagram-E4405F?style=for-the-badge&logo=instagram&logoColor=white" target="_blank"></a>
  <a href="https://www.linkedin.com/in/nicolas-albu/" target="_blank"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a>
  <a href="mailto:codeprograma@gmail.com" target="_blank"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
</div>

&nbsp;<div align="center">
  [![Spotify](https://novatorem.vercel.app/api/spotify?background_color=0d1117&border_color=ffffff)](https://open.spotify.com/user/nicolasalbuquerque581)
</div>

##

### :computer: **Código do Programador**

```python
from abc import ABC, abstractmethod


class Human(ABC):
    """Class representing a human"""
    
    def __init__(self, name: str, age: int):
        self.__name: str = name
        self.__age: int = age
    
    @abstractmethod
    def is_sleep(self) -> bool:
        pass

    def get_name(self) -> str:
        return self.__name
    
    def get_age(self) -> int:
        return self.__age
    
    def __str__(self) -> str:
        return f"Human {self.get_name()} of {self.get_age()} years old"

class Programmer(Human):
    """Class representing a programmer"""
    
    def __init__(self, programmer_data: dict[str, str | bool]):
        super().__init__(programmer_data['name'], programmer_data['age'])
        
        self.__especialization: str = programmer_data['especialization']
        self.__have_coffee: bool = programmer_data['have_coffee']
        
        if self.__especialization.lower() == "backend" and not self.__have_coffee:
            raise Exception(f"{self.__str__()} failed! :(")
                
    def is_sleep(self) -> bool:
        return False if self.__especialization.lower() == "backend" else True

    def __str__(self) -> str:
        return super().__str__().replace("Human", "Programmer")

if __name__ == '__main__':
    programmer_data: dict[str, str | int | bool] = {
        "name": "Nícolas",
        "age": 17,
        "especialization": "backend",
        "have_coffee": False,
    }
    new_programmer = Programmer(programmer_data)
```

##

### :man_technologist: **Tecnologias**

<div style="display: inline_block"><br>
  <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">
  <img align="center" alt="Java" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/java/java-original.svg">
  <img align="center" alt="Javascript" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg">
  <img align="center" alt="Arduino" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/arduino/arduino-original.svg">
  <img align="center" alt="Django" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/django/django-plain.svg">
  <img align="center" alt="Flask" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/flask/flask-original.svg">
  <img align="center" alt="FastAPI" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/fastapi/fastapi-original.svg">
  <img align="center" alt="Spring Framework" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/spring/spring-original.svg">
  <img align="center" alt="Express.js" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/express/express-original.svg">
  <img align="center" alt="Oracle" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/oracle/oracle-original.svg">
  <img align="center" alt="PostgreSQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg">
  <img align="center" alt="MySQL" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg">
  <img align="center" alt="Redis" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/redis/redis-original.svg">
  
</div>

  ##

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/Nicolas-albu/Nicolas-albu/blob/output/github-contribution-grid-snake.gif" />
</picture>