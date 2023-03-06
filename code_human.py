from abc import ABC, abstractmethod


class Human(ABC):
    """Class representing a human"""
    
    def __init__(self, name: str, age: int):
        """characteristics of a human

        Args:
            name (str): name of the human
            age (int): age of the human
        """
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
        """add characteristics of a programmer

        Args:
            programmer_data (dict[str, str  |  bool]): characteristics of a programmer

        Raises:
            Exception: when the programmer is back-end and doesn't have coffee
        """
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