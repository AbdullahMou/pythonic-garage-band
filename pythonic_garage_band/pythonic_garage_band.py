from abc import ABC, abstractmethod 
class Band :
    
    def __init__(self,name):
        self.name=name
        self.members=[]

    def __str__(self):
        return f'Band <{self.name}>'

    def __repr__(self):
        return f" '{self.name}' "



# ------------------------------------------------------


class Musician :
    def __init__(selfl,name):
        selfl.name=name

    @staticmethod
    def play_solo():
        return "i'm very interested in play solo"    

    @abstractmethod
    def greet(abc):
        print(f"hello I am {abc.name}")

   
# ------------------------------------------------------

class Bassist(Musician):
    def __str__(abc):
        return f'My name is {abc.name} and I play bass'

    def __repr__(self):
        return f" '{self.name}' "
    
    @staticmethod
    def play_solo():
        return "i'm not very interested in play solo"
    
    @staticmethod
    def get_instrument():
        return "bass"

# -----------------------------------------------------------------

class Drummer(Musician):
    def __str__(self):
        return f'My name is {self.name} and I play drums'

    def __repr__(self):
        return f" '{self.name}' "
    
    @staticmethod
    def play_solo():
        return "i'm very interested in play solo"
    
    @staticmethod
    def get_instrument():
        return "drums"


# -----------------------------------------------------------------

class Guitarist(Musician):
    def __str__(abc):
        return f'My name is {abc.name} and I play guitar'

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"
        
    
    @staticmethod
    def play_solo():
        Musician.play_solo()
    
    @staticmethod
    def get_instrument():
        return "guitar"


# ------------------------------------------------------


if __name__ == "__main__":
    band =Band('band11')
    print(band)
            
    Guitar= Guitarist("Guitarist11")
    print(Guitar)
    print(Guitarist.play_solo())
    print(Guitarist.get_instrument())
