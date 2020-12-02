from abc import ABC, abstractmethod


class Band():

    bands = []
    def __init__(self,name,members):
        self.name=name
        self.members=members
        Band.bands.append(self)

    def to_list(cls):
        return cls.bands

    def __str__(self):
        return f"Band <{self.name}>"
    
    def __repr__(self):
        return f" '{self.name}' "

    def play_solos(self):
        result=''
        for i in self.members:
            result+=f"this is {i},{i.play_solo()}\n"
        return result    


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

        return f' {self.name}'

    
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

        return f'{self.name}'

    
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
        return f'{self.name} '

    def __repr__(self) :
        return f'{self.name} '


    def get_instrument(self) :
        return "i am a Drummer !!? "

    def play_solo(self) :
        return "i am playing on my drums "    


if __name__ == "__main__":

    jhon=Drummer('jhon')
    rania=Guitarist('rania')
    adam=Bassist('adam')
    
    garag=Band('garag',[jhon,rania,adam])

    print(garag.play_solos())
    
