from abc import ABC, abstractmethod


class Band():

    bands = []
    def __init__(self,name):
        self.name=name
        Band.bands.append(self)

    def to_list(cls):
        return cls.bands

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "


class Musician():
  
    
    def __init__(self, name):
        self.name=name
        
    def __str__(self) :
        '''
        this str method from super class to make every sub class have str method
        '''
        return f'Musican class  str <{self.name} >'


    def __repr__(self):

        return f'{self.name} '

    def __str__(self):
        return f'I am a {self.name} '

    @abstractmethod


    def get_instrument(self):
        '''
        this get_instrument method from super class to make every sub class have 
        get_instrument method
        '''
        pass   

    @abstractmethod
    def play_solo(self) : 
        pass   


class Guitarist(Musician) :
    def __init__(self, name ):

         super().__init__(name)


    def __str__(self) :

        return f' class   <{self.name} >'

    
    def __repr__(self) :

        return f'{self.name} '


    def get_instrument(self) :

        return "i am a Guitarist  "

    def play_solo(self) :

        return "i am playing on my guitar "    



class Bassist(Musician):
    def __init__(self, name ):

         super().__init__(name)


    def __str__(self) :

        return f' class   <{self.name} >'

    
    def __repr__(self) :

        return f'{self.name} '


    def get_instrument(self):

        return "i am a Bassist  "

    def play_solo(self) :


        return "i am playing on my bass "    


class Drummer(Musician):

    def __init__(self, name ):
         super().__init__(name)

    def __str__(self) :
        return f' class   <{self.name} >'

    def __repr__(self) :
        return f'{self.name} '


    def get_instrument(self) :
        return "i am a Drummer !!? "

    def play_solo(self) :
        return "i am playing on my drums "    


if __name__ == "__main__":

    rania = Bassist('rania')
    print(rania)
    print(rania.get_instrument())
    print(rania.play_solo())
    meatal=Band('metal')
    rab=Band('rab')
    print(meatal.to_list())
    
